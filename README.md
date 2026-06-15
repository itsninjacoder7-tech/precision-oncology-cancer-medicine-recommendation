# 🧬 Precision Oncology Medicine Recommendation System

## Overview

The Precision Oncology Medicine Recommendation System is an AI-powered healthcare application developed during a Summer Internship at IIITDM Kurnool. The project combines Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), FAISS vector search, and Precision Oncology knowledge bases to provide personalized cancer treatment recommendations based on patient mutations, cancer types, and clinical information.

The system retrieves relevant oncology evidence from a curated knowledge base and generates clinically relevant recommendations using an LLM. It also supports file uploads such as PDF, CSV, and TXT reports through a web-based interface.

---

## Features

* AI-powered Precision Oncology recommendations
* Retrieval-Augmented Generation (RAG) architecture
* FAISS vector database for semantic search
* Support for PDF, CSV, and TXT medical reports
* Large Language Model integration using Groq API
* Flask-based web application
* Oncology knowledge retrieval and evidence generation
* Interactive healthcare dashboard
* Scalable and modular project architecture

---

## Technologies Used

* Python
* Flask
* FAISS
* Sentence Transformers
* Groq API
* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* HTML, CSS
* Pandas
* NumPy

---

## Project Structure

```text
Precision_Oncology_Template/
│
├── app.py
├── main.py
├── .env
├── requirements.txt
│
├── llm/
│   ├── inference.py
│   ├── run_LLM.py
│   ├── run_LLM_batch.py
│   ├── run_RAGLLM.py
│   └── run_RAGLLM_batch.py
│
├── context_retriever/
│   └── hybrid_search.py
│
├── data/
│   ├── fda_context.json
│   └── latest_db/
│       └── indexes/
│           └── oncology.faiss
│
├── templates/
│   └── index.html
│
├── uploads/
├── output/
└── report_generator/
```

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Precision-Oncology-System.git

cd Precision-Oncology-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Build FAISS Index

```bash
python build_faiss.py
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Usage

1. Upload a PDF, CSV, or TXT medical report.
2. Enter an oncology-related query.
3. Click **Generate AI Recommendation**.
4. The system retrieves relevant oncology evidence.
5. The LLM generates personalized treatment recommendations.
6. Results are displayed through an interactive dashboard.

---

## Sample Query

```text
HER2 positive breast cancer patient requiring treatment recommendation
```

## Sample Output

```text
Mutation: HER2 Amplification

Recommended Drug:
Trastuzumab

FDA Evidence:
Approved targeted therapy for HER2-positive breast cancer.

Clinical Explanation:
Trastuzumab targets HER2 receptors and improves survival outcomes.
```

---

## Learning Outcomes

* Understanding of Precision Oncology
* Experience with Deep Learning and LLMs
* Knowledge of Retrieval-Augmented Generation
* FAISS vector database implementation
* Healthcare AI application development
* Web application deployment using Flask

---

## Future Enhancements

* Real-time clinical guideline integration
* Multi-cancer support
* Advanced patient report analytics
* PDF report generation
* Explainable AI recommendations
* Multi-modal medical data support
* Clinical trial matching system

---

## Internship Details

**Organization:** Indian Institute of Information Technology Design and Manufacturing (IIITDM), Kurnool

**Department:** Computer Science and Engineering

**Mentor:** Dr. Chandra Mohan

**Project Title:** Deep Learning Based Precision Oncology Medicine Recommendation System

**Duration:** Two-Month Summer Internship Program

---

## License

This project is developed for educational and research purposes under the Summer Internship Program at IIITDM Kurnool.
By 
PAGADALA VENKATA RAMANA
G PULLAREDDY ENGINEERING COLLEGE,KURNOOL.
CSD(DATA SCIENCE).
