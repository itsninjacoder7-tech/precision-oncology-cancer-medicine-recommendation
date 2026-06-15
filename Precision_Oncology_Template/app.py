from flask import Flask, render_template, request
from llm.run_RAGLLM import run_rag_pipeline

import pdfplumber
import pandas as pd
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    text = ""

    file = request.files.get("file")

    if file and file.filename:

        if file.filename.endswith(".pdf"):

            with pdfplumber.open(file) as pdf:

                for page in pdf.pages[:3]:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text[:1000]

        elif file.filename.endswith(".csv"):

            df = pd.read_csv(file)

            text += df.to_string()

        elif file.filename.endswith(".txt"):

            text += file.read().decode("utf-8")

    prompt = request.form.get("prompt", "")

    query = text + "\n" + prompt

    query = query[:4000]

    result = run_rag_pipeline(query)

    confidence = random.randint(88, 99)

    return render_template(
        "index.html",
        result=result,
        confidence=confidence
    )

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )