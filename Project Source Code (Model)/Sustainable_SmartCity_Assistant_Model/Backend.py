import os, json, torch
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import PyPDF2
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest
from dotenv import load_dotenv

# === Load environment ===
load_dotenv()
HUGGINGFACE_HUB_TOKEN = os.getenv("HUGGINGFACE_HUB_TOKEN")
MODEL_NAME = "ibm-granite/granite-3.3-2b-instruct"
CITY_DATA_PATH =r"#Enter Your data/Cities.json entire path path#"    #Example: r"C:\Users\AKP\Desktop\AI\Sustainable_SmartCity_Assistant_Model\data\cities.json"

# === Load Granite Model ===
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HUGGINGFACE_HUB_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        token=HUGGINGFACE_HUB_TOKEN,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

model_pipeline = load_model()

# === City Data ===
def load_all_cities():
    if not os.path.exists(CITY_DATA_PATH):
        return {}
    with open(CITY_DATA_PATH, "r") as f:
        return json.load(f)

def save_all_cities(data):
    with open(CITY_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)

def get_city_data(name):
    return load_all_cities().get(name, {})

def add_or_update_city(name, new_data):
    data = load_all_cities()
    new_data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data[name] = new_data
    save_all_cities(data)

def delete_city(name):
    data = load_all_cities()
    if name in data:
        del data[name]
        save_all_cities(data)

# === AQI Category
def get_aqi_category(aqi):
    try:
        aqi = int(aqi)
        if aqi <= 50:
            return "Good", "#00FF00"
        elif aqi <= 100:
            return "Moderate", "#FFFF00"
        elif aqi <= 150:
            return "Unhealthy (Sensitive)", "#FFA500"
        elif aqi <= 200:
            return "Unhealthy", "#FF0000"
        elif aqi <= 300:
            return "Very Unhealthy", "#800080"
        else:
            return "Hazardous", "#800000"
    except:
        return "Unknown", "#888888"

# === Alerts
def check_alerts(city_data):
    alerts = []
    try:
        aqi = int(city_data.get("environment", {}).get("value", 0))
        if aqi > 150:
            alerts.append("⚠️ AQI Warning: Air quality is poor.")
        energy = int(city_data.get("energy", {}).get("value", "0").replace("%", ""))
        if energy > 85:
            alerts.append("⚡ High energy usage detected.")
        waste = city_data.get("waste", {}).get("value", "").lower()
        if "high" in waste:
            alerts.append("🚮 Waste levels are high.")
    except:
        pass
    return alerts

# === Granite LLM
def ask_granite(prompt):
    result = model_pipeline(prompt, max_new_tokens=400, temperature=0.7)[0]["generated_text"]
    return result.strip()

def ask_city_assistant(city, question):
    info = get_city_data(city)
    if not info:
        return "No data found for the selected city."

    context = "\n".join([f"{k}: {v.get('value')}" for k, v in info.items()])

    prompt = f"""
You are a smart city assistant. Use ONLY the information below to answer the user's question. 
Avoid summaries or extra insights. Just give a short, direct answer.

City: {city}
City Data:
{context}

User Question: {question}

Answer:
"""
    result = model_pipeline(prompt, max_new_tokens=200, temperature=0.3)[0]["generated_text"]
    return result.replace(prompt, "").strip()


# === Document Upload
def extract_text_from_file(file):
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() or "" for page in reader.pages])
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""

def summarize_document(text):
    prompt = f"Summarize this urban policy document in 5 short bullet points:\n\n{text[:4000]}"
    output = model_pipeline(prompt, max_new_tokens=300, temperature=0.5)[0]["generated_text"]
    return output.replace(prompt, "").strip()

def qna_from_document(text, question):
    prompt = f"""Answer the question using ONLY this document content:

{text[:3500]}

Question: {question}
"""
    output = model_pipeline(prompt, max_new_tokens=300)[0]["generated_text"]
    return output.replace(prompt, "").strip()

# === Eco Tip Generator from CSV
def generate_eco_tip_from_csv(file, topic):
    df = pd.read_csv(file)
    if 'category' not in df.columns or 'tip' not in df.columns:
        return "❌ CSV must contain 'category' and 'tip' columns."

    filtered = df[df['category'].str.contains(topic, case=False, na=False)]
    if filtered.empty:
        return f"⚠️ No tips found for topic: {topic}"

    tips = filtered['tip'].dropna().unique().tolist()[:3]
    return f"💡 Eco Tips for **{topic.title()}**:\n" + "\n".join([f"🌿 {t}" for t in tips])

# === Forecasting
def forecast_kpi(file, category):
    df = pd.read_csv(file)
    if 'timestamp' not in df.columns or 'value' not in df.columns:
        raise ValueError("Invalid CSV format. Expected 'timestamp' and 'value' columns.")

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.sort_values('timestamp', inplace=True)
    df['t'] = range(len(df))
    model = LinearRegression()
    model.fit(df[['t']], df['value'])

    future = pd.DataFrame({'t': range(len(df), len(df) + 5)})
    df_future = pd.DataFrame()
    df_future['timestamp'] = pd.date_range(start=df['timestamp'].iloc[-1], periods=6, freq='D')[1:]
    df_future['predicted_value'] = model.predict(future)

    return df_future

# === Anomaly Detection
def detect_anomalies(file, category):
    df = pd.read_csv(file)
    if 'timestamp' not in df.columns or 'value' not in df.columns:
        raise ValueError("Invalid CSV format. Expected 'timestamp' and 'value' columns.")

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df.dropna(inplace=True)

    model = IsolationForest(n_estimators=100, contamination=0.1)
    df['anomaly'] = model.fit_predict(df[['value']])
    anomalies = df[df['anomaly'] == -1].drop(columns='anomaly')
    return anomalies
