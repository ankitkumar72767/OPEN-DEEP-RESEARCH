# 🔎 OpenDeepResearcher — Agentic AI Research Assistant (Streamlit Edition)

OpenDeepResearcher is an AI-powered research system that works like a human researcher.  
You provide a topic → the system automatically **plans**, **searches**, **analyzes**, and **writes** a structured research report using multi-agent AI workflows.

It includes:

 ⭐ Planner Agent  
 ⭐ Web Search Agent (Tavily)  
 ⭐ Writer Agent (LLM)  
 ⭐ Session History & Memory  
 ⭐ Streamlit UI  
 ⭐ Multi-format export (Markdown / JSON / PDF)



##  Key Features

### 🔹 Planner Agent  
Breaks your topic into well-structured sub-questions.

### 🔹 Searcher Agent (Tavily)
Fetches real-time web information including:
- URLs  
- Titles  
- Summaries  
- Timestamps  

### 🔹 Writer Agent (LLM)
Generates:
- Short summaries  
- Long academic-style reports  
- Multi-language output  

Supports:
-  LM Studio  
-  Ollama  
-  OpenAI-compatible APIs  

### 🔹 Streamlit UI
Modern UI with:
- Glassmorphism design  
- Neon gradient buttons  
- Sidebar configuration  
- Clean report viewer  
- Session history  

### 🔹 Export Options
Download results as:
- 📄 Markdown  
- 📄 JSON  
- 📄 PDF  



## 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| Frontend UI | Streamlit |
| LLM Workflow | LangGraph |
| LLM Integration | LangChain |
| Web Search API | Tavily |
| Local LLM Support | LM Studio / Ollama |
| Language | Python 3.10+ |



## 📁 Folder Structure



<img width="468" height="393" alt="image" src="https://github.com/user-attachments/assets/a065c418-9dd3-420a-8d96-63c1b49dd78d" />

## ⚙️ Installation Guide

### 1️⃣ Create Virtual Environment



## ⚙️ Installation Guide

### 1️⃣ Create Virtual Environment
python -m venv .venv


Activate environment:

**Windows**
.venv\Scripts\activate


**Mac/Linux**
source .venv/bin/activate


### 2️⃣ Install Dependencies
pip install -r requirements.txt



### 3️⃣ Add Environment Variables

Create a `.env` file:

TAVILY_API_KEY=your_tavily_key
OPENAI_API_BASE=http://127.0.0.1:1234/v1
OPENAI_API_KEY=test


### 4️⃣ Run the App

streamlit run app.py


Open:
http://localhost:8501



## 🧩 How It Works

1. User enters a topic  
2. Planner Agent generates sub-questions  
3. Searcher Agent fetches fresh online data  
4. Writer Agent synthesizes the content  
5. UI displays structured final report  
6. User downloads output in 3 formats  



## 📄 Example Topics

- AI in Healthcare  
- Climate Change  
- Cybersecurity Trends  
- Electric Vehicles  
- Blockchain / Web 3.0  


##  Current Project Status

-  Fully functional  
-   Multi-agent pipeline complete  
-  Tavily + LM Studio integrated  
-  UI finished  
-  History working  
-  Multi-language supported  
-  PDF / JSON / Markdown export  



## 🔮 Future Improvements

- APA / IEEE citations  
- PPT export  
- Charts & graphs  
- Voice input  
- Audio summary  



## 👨‍💻 Author

**Ankit Kumar – CS-AIML**  
Developer of OpenDeepResearcher – a full agentic LLM research system.

GitHub: https://github.com/ankitkumar72767  


## ⭐ Support  
If you like this project, please ⭐ star the repository!
