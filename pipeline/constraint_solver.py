import openai

def solve_constraint_question(context, question):
    prompt = f"Given this information:\n{context}\nRank the options relevant to this question:\n{question}\nThen choose the correct answer."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
