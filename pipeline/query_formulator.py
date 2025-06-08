import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def formulate_query(context, question):
    prompt = f"""
You are a Prolog expert. Given the following context and question, write a Prolog query that would retrieve the correct answer.

Requirements:
- Use lowercase constants (e.g., 'alice', 'cheetah')
- Use predicates that naturally match the context (e.g., kind(X), fast(X), helpful(X))
- Do not explain your answer
- Return only the query — no extra text or formatting

Context:
{context}

Question:
{question}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt.strip()}
        ]
    )

    query = response["choices"][0]["message"]["content"].strip()
    query = query.rstrip(".")
    return query
