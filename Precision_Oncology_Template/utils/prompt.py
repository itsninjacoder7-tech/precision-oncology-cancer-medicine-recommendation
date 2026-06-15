def build_prompt(context,
                 question):

    return f"""
You are a precision oncology specialist.

Retrieved Evidence:
{context}

Patient Query:
{question}

Provide:
1. Mutation
2. Recommended Drug
3. FDA Evidence
4. Explanation
"""