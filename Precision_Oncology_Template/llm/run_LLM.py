from llm.inference import generate

def run_llm_pipeline(query):

    prompt = f"""
You are an oncology expert.

Question:
{query}
"""

    answer = generate(prompt)

    print(answer)

    return answer