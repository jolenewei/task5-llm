import openai
import os

def generate_prolog_facts(context):
    prompt = f"""Convert the following context into Prolog facts and rules.
Use these exact predicate names:
- kind(X) for statements about someone being kind
- helpful(X) for statements about someone being helpful

Context:
{context}

Give only the Prolog code:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
