import pandas as pd
from llm.run_LLM import run_llm_pipeline

def run_batch(csv_file):

    df = pd.read_csv(csv_file)

    outputs = []

    for q in df["query"]:
        outputs.append(
            run_llm_pipeline(q)
        )

    df["answer"] = outputs

    df.to_csv(
        "llm_results.csv",
        index=False
    )