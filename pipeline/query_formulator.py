import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def formulate_query(context, question):
    prompt = f"""Context:\n{context}\n\nQuestion:\n{question}\n\n
    Write a Prolog query (no explanation) that would answer this question given the context."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"].strip()

