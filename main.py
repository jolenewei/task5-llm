from pipeline.classifier import classify_question
from pipeline.prolog_generator import generate_prolog_facts
from pipeline.query_formulator import formulate_query
from pipeline.executor import execute_prolog_query
from pipeline.constraint_solver import solve_constraint_question
from dotenv import load_dotenv
import json
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def rewrite_question(context, question):
    prompt = f"""Context: {context}
Question: {question}

The above question could not be classified as a logic or ranking task. Please rewrite the question to clarify what type of task it is (logic or ranking), without changing its original meaning."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

def main():
    with open("data/examples.json") as f:
        data = json.load(f)

    results = []

    for ex in data:
        context = ex["context"]
        original_question = ex["question"]
        question = original_question

        retry_count = 0
        classification = classify_question(context, question)

        while classification == "unknown" and retry_count < 5:
            print(f"Retry {retry_count + 1}: Rewriting question...")
            question = rewrite_question(context, question)
            classification = classify_question(context, question)
            retry_count += 1
        if classification == "logic":
            facts = generate_prolog_facts(context)
            query = formulate_query(context, question)
            answer = execute_prolog_query(facts, query)
        elif classification == "ranking":
            answer = solve_constraint_question(context, question)
        else:
            answer = "Unknown"

        print(f"--- {ex['id']} ---")
        print(f"Q: {question}")
        print(f"Predicted: {answer} | Ground Truth: {ex.get('answer', 'N/A')}\n")

        results.append({
            "id": ex["id"],
            "original_question": original_question,
            "final_question_used": question,
            "classification": classification,
            "predicted": answer,
            "answer": ex.get("answer", "N/A")
        })

    os.makedirs("results", exist_ok=True)
    with open("results/results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()