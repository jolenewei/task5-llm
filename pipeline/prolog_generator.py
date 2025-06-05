import openai
import os

def generate_prolog_facts(context):
    prompt = f"Convert this context into Prolog facts:\n{context}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]