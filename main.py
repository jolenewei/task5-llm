from pipeline.classifier import classify_question
from pipeline.prolog_generator import generate_prolog_facts
from pipeline.query_formulator import formulate_query
from pipeline.executor import execute_prolog_query
from pipeline.constraint_solver import solve_constraint_question
from dotenv import load_dotenv
import json

load_dotenv()

def main():
    with open("data/examples.json") as f:
        data = json.load(f)

    results = []

    for ex in data:
        context = ex["context"]
        question = ex["question"]

        classification = classify_question(context, question)
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
            "question": question,
            "predicted": answer,
            "answer": ex.get("answer", "N/A")
        })

    with open("results/results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()