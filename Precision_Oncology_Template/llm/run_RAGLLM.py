from context_retriever.hybrid_search import retrieve
from utils.prompt import build_prompt
from llm.inference import generate

def run_rag_pipeline(query):

    context = retrieve(query)

    prompt = build_prompt(
        context,
        query
    )

    answer = generate(prompt)

    print(answer)

    return answer