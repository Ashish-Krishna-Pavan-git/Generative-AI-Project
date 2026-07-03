# Generative-AI-Project  

**Author:** Ashish Krishna Pavan Gade  
**Email:** ashishkrishnapavan@gmail.com  
**Website:** https://akpghub.live  
**Contact:** ashish@akpghub.live  

---

## Table of Contents  

1. [Project Overview](#project-overview)  
2. [Key Features](#key-features)  
3. [Folder Structure](#folder-structure)  
4. [Prerequisites & Setup](#prerequisites--setup)  
5. [Running the App](#running-the-app)  
6. [User Guide](#user-guide)  
7. [Technology Stack](#technology-stack)  
8. [Final Project Report](#final-project-report)  
9. [License & Acknowledgements](#license--acknowledgements)  

---

## 1. Project Overview  

The **Sustainable Smart City Assistant** is an AI‑enhanced, Streamlit‑based dashboard that enables city planners, residents, and service staff to interact with real‑time KPI data, receive AI‑generated insights, and make data‑driven decisions for sustainability.  

---  

## 2. Key Features  

| Feature | Description |
|---------|-------------|
| **Dashboard** | Interactive charts, maps, KPI cards, and alerts for energy, water, waste, traffic, health, etc. |
| **Chat Assistant** | LLM‑powered conversational interface for queries about city data or civic matters. |
| **Eco‑Tip Generator** | One‑click generation of sustainability recommendations based on city KPIs. |
| **Document Summariser** | Upload PDF/DOCX/TXT → concise summary with key bullet points. |
| **City Data Manager** | Add, edit, or delete city KPI CSV/JSON files. |
| **Forecasting** | Predict future KPI values (30‑day or 90‑day) with confidence intervals. |
| **Anomaly Detection** | Statistical and ML‑based detection of outliers in KPI streams. |
| **Theme Selector** | Switch between dark, light, professional, and eco‑green UI themes. |
| **Export** | Download charts (PNG/PDF) or KPI tables (CSV). |

---  

## 3. Folder Structure  

```
/app/sharedFiles/Generative-AI-Project/  
├─ Project Documentation/  
│   ├─ Ideation Phase/  
│   ├─ Performance Testing/  
│   ├─ Project Design Phase/  
│   ├─ Project Planning Phase/  
│   ├─ Requirement Analysis/  
│   ├─ Final Projet Report.pdf   (updated)  
│   └─ Final Projet Report.docx  (updated)  
├─ Project Source Code (Model)/  
│   └─ Sustainable_SmartCity_Assistant_Model/  
│       ├─ backend.py  
│       ├─ ui.py  
│       ├─ requirements.txt  
│       ├─ .env.txt   (rename to .env)  
│       └─ data/  
├─ README.md   (updated)  
└─ LICENSE   (updated)  
```

---  

## 4. Prerequisites & Setup  

1. **Clone the repository** (or download the files).  
2. **Create a Python virtual environment** (optional but recommended):  

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```  

3. **Install dependencies:**  

   ```bash
   pip install -r Project\ Source\ Code\ \(Model\)/Sustainable_SmartCity_Assistant_Model/requirements.txt
   ```  

4. **Set up environment variables:**  

   - Open `Project Source Code (Model)/.env.txt`  
   - Replace the placeholder with your Hugging Face token:  

     ```ini
     HUGGINGFACE_HUB_TOKEN=your_token_here
     ```  

   - Save the file as `.env` (the system will read it automatically).  

5. **Adjust data path (if needed):**  

   Edit `Project Source Code (Model)/backend.py` and set  

   ```python
   CITY_DATA_PATH = "Project Source Code (Model)/data/cities.json"
   ```  

   (or point to the appropriate CSV/JSON files).  

---  

## 5. Running the Application  

```bash
cd Project\ Source\ Code\ \(Model\)/Sustainable_SmartCity_Assistant_Model
streamlit run ui.py
```  

Open `http://localhost:8501` in your browser.  

---  

## 6. User Guide  

1. **Dashboard** – View real‑time KPI visualisations and receive alerts.  
2. **Chat** – Type a question (e.g., “What is the current water usage trend?”).  
3. **Eco‑Tip** – Click “Generate Eco‑Tip” for personalized sustainability advice.  
3. **Document Summariser** – Upload a PDF/DOCX/TXT file → receive a concise summary.  
4. **Data Manager** – Add new KPI files or edit existing ones.  
5. **Forecast** – Choose a KPI and horizon (30 days / 90 days) to see predictions.  
6. **Anomalies** – Detect unusual spikes/dips in KPI values.  
7. **Theme** – Change UI appearance via the Settings sidebar.  

---  

## 7. Technology Stack  

| Layer | Technology |
|-------|------------|
| **Frontend** | Streamlit (Python) |
| **Backend** | FastAPI (optional) + Pandas for data handling |
| **LLM** | Hugging Face Transformers (20B model) |
| **Data Storage** | CSV / JSON files (local) |
| **Caching** | Streamlit session state + pickled model caches |
| **Python** | 3.11+ |
| **Theme** | Custom CSS + Streamlit theming |

---  

## 8. Final Project Report  

The **Final Project Report** (PDF and DOCX) contains:  

- Executive summary and problem statement  
- Solution architecture diagram and implementation details  
- Code structure, module breakdown, and API endpoints  
- Evaluation results (accuracy, latency, user study)  
- Demo screenshots, video link, and future work  

The updated report files are located in `Project Documentation/`. Open them with any PDF/DOCX viewer.  

---  

## 9. License & Acknowledgements  

**License:** MIT License (see `LICENSE` file).  

**Acknowledgements:**  

- Hugging Face Transformers team  
- Streamlit community  
- City KPI data providers  
- Collaborators in the Sustainable Computing Lab  

---  

## 10. Contact  

For questions, suggestions, or support, please email **ashishkrishnapavan@gmail.com** or message **ashish@akpghub.live**.  

---  

*© 2026 Ashish Krishna Pavan Gade. All rights reserved.*  
```