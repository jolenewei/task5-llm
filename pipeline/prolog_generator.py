import openai
import os
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

def clean_prolog(text: str) -> str:
    lines = text.splitlines()
    out = []
    for l in lines:
        l = l.strip().strip("`")  # drop backticks
        if not l or l.startswith('%'):  # skip empties/comments
            continue
        if not l.endswith('.'):
            l += '.'
        out.append(l)
    return "\n".join(out)

def generate_prolog_facts(context: str) -> str:
    prompt = (
        "Convert the following context into Prolog facts and rules.\n\n"
        "Only output Prolog clauses (lowercase predicates), one per line.\n"
        "Don't include any natural language or explanation.\n\n"
        "Context:\n"
        f"{context}\n"
    )
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    raw = resp["choices"][0]["message"]["content"]
    return clean_prolog(raw)

