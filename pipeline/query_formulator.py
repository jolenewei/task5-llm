import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def formulate_query(context, question):
    prompt = f"""
Context:
{context}

Question:
{question}

Please write a **Prolog query** that uses only the following predicates:
- kind(X)
- helpful(X)

Use lowercase constants (e.g., 'alice') and match exactly the facts that would come from this context.
Return only the query (no explanation or extra formatting).
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt.strip()}
        ]
    )

    return response["choices"][0]["message"]["content"].strip()