import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_question(context, question):
    prompt = f"Context:\n{context}\nQuestion:\n{question}\nClassify this question as one of: logic, ranking, unknown."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    classification = response["choices"][0]["message"]["content"].strip().lower()
    return classification if classification in ["logic", "ranking"] else "unknown"
