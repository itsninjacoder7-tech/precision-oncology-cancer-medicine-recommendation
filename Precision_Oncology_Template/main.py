import argparse
from llm.run_LLM import run_llm_pipeline
from llm.run_RAGLLM import run_rag_pipeline

parser = argparse.ArgumentParser()

parser.add_argument("--mode",
                    choices=["llm","rag-llm"],
                    required=True)

parser.add_argument("--query",
                    required=True)

args = parser.parse_args()

if args.mode == "llm":
    run_llm_pipeline(args.query)

elif args.mode == "rag-llm":
    run_rag_pipeline(args.query)