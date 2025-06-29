# Generative-AI-Project

Hi, I'm **Ashish Krishna Pavan**.  
This is a **Generative AI project** where I built a **Sustainable Smart City Assistant** with the following powerful features:

###  Functionalities Included:
1.  **Dashboard** — Displays city metrics and smart alerts.
2.  **Chat Assistant** — Answers questions based on selected city data and general queries.
3.  **Eco Tips Generator** — Provides eco-friendly advice.
4.  **Document Summarizer** — Summarizes and answers questions from uploaded documents.
5.  **City Data Manager** — Add, edit, and delete city data.
6.  **Forecasting** — Predicts future KPI values based on CSV input.
7.  **Anomaly Detection** — Identifies anomalies in KPI data.
8.  **Theme Selector** — Allows users to switch between multiple glowing & professional UI themes.

---

##  Repository Folder Structure

Once you’re inside the repository:  
**Ashish-Krishna-Pavan-git / Generative-AI-Project**

You will find the following files and folders:

### Top-Level Contents:
1. **Project Documentation** *(📂 Folder)*
2. **Project Source Code (Model)** *(📂 Folder)*
3. `LICENSE`
4. `README.md` *(📄 You're here)*

### 🎥 Project Demo Video:
[Click here to watch the working demo](https://drive.google.com/drive/u/1/folders/1tc0BGUZgsQBk94P2XsP5zevpV-LeclmR)  

---

## 📚 Project Documentation Folder Structure

### 1) Ideation Phase:
- a) Brainstorming - Idea Generation - Prioritization (Doc + PDF)
- b) Define Problem Statements (Doc + PDF)
- c) Empathy Map Canvas (Doc + PDF)

### 2) Performance Testing:
- 🧪 `GenAI Functional & Performance Testing` (Doc + PDF)

### 3) Project Design Phase:
- a) Problem - Solution Fit (Doc + PDF)
- b) Proposed Solution (Doc + PDF)
- c) Solution Architecture (Doc + PDF)

### 4) Project Planning Phase:
- 📋 Project Planning Template (Doc + PDF)

### 5) Requirement Analysis:
- a) Customer Journey Map (Doc + PDF)
- b) Data Flow Diagrams and User Stories (Doc + PDF)
- c) Solution Requirements (Doc + PDF)
- d) Technology Stack Template (Doc + PDF)

### 6) Final Project Report:
Includes complete write-up from start to end with:
- Output screenshots
- System diagrams
- GitHub & demo video links

---

## ⚙️ Project Source Code (Model)

Path:  
`Project Source Code (Model)/Sustainable_SmartCity_Assistant_Model/`

### Inside you'll find:
1. 📂 `Output Files`
2. 📂 `Testing Files`
3. 📂 `data`
4. 🧠 `Backend.py`
5. 🎨 `Frontend(UI).py`
6. 📦 `requirements.txt`
7. 🔐 `.env.txt` *(Rename to `.env` before running)*

---

## 🚀 How to Run the Application:

### Step-by-step Setup:

1. **Download all 7 files** from the folder mentioned above.
2. Open terminal / command prompt and install required packages:
   ```bash
   pip install -r requirements.txt
### ✅ Step-by-step Setup Instructions:

1. **Download all 7 files** inside the `Sustainable_SmartCity_Assistant_Model` folder.

2. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
3. **Set up `.env`:**
   - Open `.env.txt` and paste your Hugging Face token like:
     ```ini
     HUGGINGFACE_HUB_TOKEN=your_token_here
     ```
   - Save the file as `.env`.

4. **Update `cities.json` path in `Backend.py`:**
   ```python
   CITY_DATA_PATH = r"path_to_your_downloaded/data/cities.json"
   ```

5. **Run the Streamlit application:**
   ```bash
   streamlit run "Frontend(UI).py"
   ```

6. ✅ Enjoy the full-featured app in your browser!

---

### 🤝 License

This project is licensed under the **MIT License**, with the following condition:

> You are free to use, modify, and explore this application **for educational and personal use only**.  
> **Commercial use, publishing, or redistribution without explicit permission from the author is prohibited.**

---

### 📬 Contact

Feel free to reach out with questions or suggestions:  
📧 **ashishkrishnapavan@gmail.com**
