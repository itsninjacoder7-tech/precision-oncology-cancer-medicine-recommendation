import pandas as pd
from llm.run_RAGLLM import run_rag_pipeline

def run_batch(csv_file):

    df = pd.read_csv(csv_file)

    outputs = []

    for q in df["query"]:
        outputs.append(
            run_rag_pipeline(q)
        )

    df["answer"] = outputs

    df.to_csv(
        "rag_results.csv",
        index=False
    )