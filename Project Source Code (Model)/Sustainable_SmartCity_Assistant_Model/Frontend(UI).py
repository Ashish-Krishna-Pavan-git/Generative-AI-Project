import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu
from Backend import (
    load_all_cities, add_or_update_city, delete_city,
    ask_city_assistant, extract_text_from_file,
    summarize_document, qna_from_document,
    check_alerts, generate_eco_tip_from_csv, ask_granite,
    forecast_kpi, detect_anomalies, get_aqi_category
)
import pandas as pd

st.set_page_config(page_title="🌆 Smart City Assistant", layout="wide")

# === THEME CONFIG ===
THEMES = {
    "Midnight Mirage": {
        "bg": "linear-gradient(135deg,#0f0c29,#302b63,#24243e)",
        "text": "#ececec",
        "accent": "#00e5ff",
        "label_colors": {
            "Traffic": "#FF69B4", "Water Supply": "#7FFF00", "Waste Level": "#FF4500",
            "Weather": "#00CED1", "Safety": "#8A2BE2", "Feedback": "#FF1493", "Health Index": "#00FA9A", "Alerts": "#FF6347"
        }
    },
    "Charcoal Ember": {
        "bg": "linear-gradient(135deg,#1c1c1c,#2c2c2c)",
        "text": "#f0f0f0",
        "accent": "#f39c12",
        "label_colors": {
            "Traffic": "#ff9966", "Water Supply": "#99cc00", "Waste Level": "#cc3300",
            "Weather": "#66cccc", "Safety": "#9966cc", "Feedback": "#ff6699", "Health Index": "#66ff99", "Alerts": "#ff3300"
        }
    },
    "Crimson Oak": {
        "bg": "linear-gradient(135deg,#800000,#A0522D)",
        "text": "#fff2e6",
        "accent": "#ffb347",
        "label_colors": {
            "Traffic": "#ff7f50", "Water Supply": "#deb887", "Waste Level": "#b22222",
            "Weather": "#cd853f", "Safety": "#d2691e", "Feedback": "#ffdab9", "Health Index": "#f4a460", "Alerts": "#dc143c"
        }
    },
    "Tropical Haze": {
        "bg": "linear-gradient(135deg,#008080,#ffd59a)",
        "text": "#102020",
        "accent": "#ffa07a",
        "label_colors": {
            "Traffic": "#e9967a", "Water Supply": "#9acd32", "Waste Level": "#cd5c5c",
            "Weather": "#40e0d0", "Safety": "#6a5acd", "Feedback": "#fa8072", "Health Index": "#20b2aa", "Alerts": "#dc143c"
        }
    },
    "Royal Glow": {
        "bg": "linear-gradient(135deg,#4b0082,#8a2be2)",
        "text": "#f9f9f9",
        "accent": "#ee82ee",
        "label_colors": {
            "Traffic": "#db7093", "Water Supply": "#adff2f", "Waste Level": "#ff6347",
            "Weather": "#7fffd4", "Safety": "#ba55d3", "Feedback": "#ff69b4", "Health Index": "#98fb98", "Alerts": "#ff4500"
        }
    }
}

# === SIDEBAR ===
with st.sidebar:
    theme_name = st.selectbox("🎨 Select Theme", list(THEMES.keys()), key="theme_selector")
    page = option_menu(
        None,
        ["Smart Hub", "City Manager", "Forecast", "Anomaly"],
        icons=["house", "building", "bar-chart", "exclamation-triangle"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#00e5ff", "color": "#0b0c10"}}
    )

# === APPLY THEME ===
theme = THEMES[theme_name]
label_colors = theme["label_colors"]

st.markdown(f"""
    <style>
    .stApp {{
        background: {theme['bg']};
        color: {theme['text']};
        animation: fadeIn 0.6s ease-in;
    }}
    @keyframes fadeIn {{ 0% {{opacity: 0;}} 100% {{opacity: 1;}} }}
    [data-testid="stSidebar"] {{ background: rgba(0,0,0,0.95); }}
    h1, h4, h2, h3, h5 {{
        color: {theme['accent']};
        text-shadow: 0 0 12px {theme['accent']}66;
    }}
    .metric-box {{
        background: rgba(255,255,255,0.06);
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 0 10px {theme['accent']}55;
    }}
    .bar-container {{
        background: #333;
        border-radius: 6px;
        overflow: hidden;
    }}
    .bar {{
        text-align:center;
        font-weight:bold;
        color: #000;
    }}
    .stButton > button {{
        background-color: {theme['accent']};
        color: #111;
        border: none;
        border-radius: 5px;
        transition: 0.2s ease-in-out;
    }}
    .stButton > button:hover {{
        transform: scale(1.05);
    }}
    </style>
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown("<h1 style='text-align:center;'>🌆 Sustainable Smart City Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Built by Ashish Krishna Pavan 💡</h4>", unsafe_allow_html=True)

# === LOAD DATA ===
cities = load_all_cities()
city_names = list(cities.keys()) or ["No Cities"]

# === SMART HUB ===
if page == "Smart Hub":
    tabs = st.tabs(["📊 Dashboard", "💬 Chat", "🌱 Eco Tips", "📄 Summarizer"])
    selected_city = st.selectbox("🏙️ Select City", city_names, key="city_selector_dashboard")
    data = cities.get(selected_city, {})

    # === Dashboard Tab ===
    with tabs[0]:
        st.subheader("📊 City Dashboard")
        rows = []
        metrics = [
            ("environment", "AQI"),
            ("energy", "Energy Usage"),
            ("traffic", "Traffic"),
            ("water", "Water Supply"),
            ("waste", "Waste Level"),
            ("weather", "Weather"),
            ("safety", "Safety"),
            ("feedback", "Feedback"),
            ("health", "Health Index"),
            ("alerts", "Alerts")
        ]
        cols = st.columns(2)
        for i, (key, label) in enumerate(metrics):
            val = data.get(key, {}).get("value", "N/A")
            display = str(val)
            color = label_colors.get(label, "#888888")

            if key == "environment":
                cat, color = get_aqi_category(val)
                display = f"{val} ({cat})"
            elif key == "energy":
                try:
                    p = int(str(val).replace("%", ""))
                    if p <= 60: cat = "Low"; color = "#00FF00"
                    elif p <= 85: cat = "Moderate"; color = "#FFA500"
                    else: cat = "High"; color = "#FF0000"
                    display = f"{val} ({cat})"
                except:
                    display = val

            rows.append({"Metric": label, "Value": display})
            try:
                num = int(str(val).replace("%", ""))
                num = max(0, min(num, 100))
                bar_html = f"""
                    <div class='metric-box'>
                      <b style='color:{color};'>{label}</b>
                      <div class='bar-container'>
                        <div class='bar' style='width:{num}%;background:{color};'>{display}</div>
                      </div>
                    </div>"""
            except:
                bar_html = f"<div class='metric-box'><b style='color:{color};'>{label}: {display}</b></div>"

            cols[i % 2].markdown(bar_html, unsafe_allow_html=True)

        st.markdown("### ⚠️ Alerts")
        alerts = check_alerts(data)
        if alerts:
            for a in alerts:
                st.error(a)
        else:
            st.success("No alerts detected.")

        df = pd.DataFrame(rows)
        st.download_button("📥 Export Dashboard CSV", df.to_csv(index=False).encode("utf-8"), "dashboard.csv", "text/csv")

    # === Chat Tab ===
    with tabs[1]:
        st.subheader("💬 Chat Assistant")
        query = st.text_input("Your question about the city")
        if st.button("Ask AI"):
            answer = ask_city_assistant(selected_city, query)
            st.success(answer)
            st.download_button("📥 Download Chat", answer, "chat.txt")

    # === Eco Tips Tab ===
    with tabs[2]:
        st.subheader("🌱 Eco Tips")
        topic = st.text_input("Enter a topic (e.g., energy, plastic)")
        csv_tip = st.file_uploader("Upload CSV with category and tip", type=["csv"])
        if st.button("Get Eco Tips"):
            tips = generate_eco_tip_from_csv(csv_tip, topic) if csv_tip else ask_granite(f"Suggest 3 eco tips for {topic}")
            st.info(tips)
            st.download_button("📥 Download Tips", tips, "eco_tips.txt")

    # === Summarizer Tab ===
    with tabs[3]:
        st.subheader("📄 Document Summarizer")
        file = st.file_uploader("Upload PDF or TXT")
        if file:
            content = extract_text_from_file(file)
            if st.button("📝 Summarize"):
                summary = summarize_document(content)
                st.write(summary)
                st.download_button("📥 Download Summary", summary, "summary.txt")
            question = st.text_input("Ask something from the document")
            if st.button("Ask from Document"):
                result = qna_from_document(content, question)
                st.write(result)
                st.download_button("📥 Download Answer", result, "answer.txt")

# === City Manager ===
elif page == "City Manager":
    st.subheader("🏗️ City Manager")
    city = st.selectbox("Select City to Edit", city_names)
    info = cities.get(city, {})
    placeholders = {
        "environment": "e.g. 85",
        "energy": "e.g. 73%",
        "traffic": "e.g. Moderate",
        "water": "e.g. Good",
        "waste": "e.g. High",
        "weather": "e.g. Sunny",
        "safety": "e.g. Safe",
        "feedback": "e.g. Positive",
        "health": "e.g. Good",
        "alerts": "e.g. AQI Warning"
    }

    with st.form("update_form"):
        updated = {}
        for k, ph in placeholders.items():
            val = info.get(k, {}).get("value", "")
            updated[k] = {
                "value": st.text_input(k.title(), val, placeholder=ph),
                "last_updated": datetime.now().strftime("%Y-%m-%d")
            }
        if st.form_submit_button("Save"):
            add_or_update_city(city, updated)
            st.success("✅ City updated successfully.")

    st.markdown("### ➕ Add New City")
    new_city = st.text_input("City Name", placeholder="e.g. Hyderabad")
    if st.button("Add City"):
        if new_city not in cities:
            add_or_update_city(new_city, {k: {"value": "0", "last_updated": datetime.now().strftime("%Y-%m-%d")} for k in placeholders})
            st.success("New city added.")
        else:
            st.warning("City already exists!")

    st.markdown("### ❌ Delete City")
    del_city = st.selectbox("Choose City to Delete", city_names)
    if st.button("Delete City"):
        delete_city(del_city)
        st.warning(f"{del_city} has been deleted.")

# === Forecast ===
elif page == "Forecast":
    st.subheader("📈 Forecast KPI")
    file = st.file_uploader("Upload KPI CSV (timestamp,value)", type=["csv"])
    category = st.selectbox("KPI Category", ["energy", "water", "traffic", "waste"])
    if st.button("Run Forecast"):
        try:
            forecast = forecast_kpi(file, category)
            st.dataframe(forecast)
            st.download_button("📥 Download Forecast", forecast.to_csv(index=False).encode(), "forecast.csv")
        except Exception as e:
            st.error(f"Forecast failed: {e}")

# === Anomaly Detection ===
elif page == "Anomaly":
    st.subheader("🚨 Anomaly Detection")
    file = st.file_uploader("Upload CSV (timestamp,value)", type=["csv"])
    category = st.selectbox("KPI Category", ["energy", "water", "traffic", "waste"])
    if st.button("Detect Anomalies"):
        try:
            anomalies = detect_anomalies(file, category)
            if anomalies.empty:
                st.success("✅ No anomalies detected.")
            else:
                st.warning("⚠️ Anomalies detected:")
                st.dataframe(anomalies)
                st.download_button("📥 Download Anomalies", anomalies.to_csv(index=False).encode(), "anomalies.csv")
        except Exception as e:
            st.error(f"Detection failed: {e}")

# === Footer ===
st.markdown(f"<footer style='text-align:center; margin-top:3rem;'>🚀 Sustainable Smart City Assistant | Created by <b>Ashish Krishna Pavan</b> 💡</footer>", unsafe_allow_html=True)
