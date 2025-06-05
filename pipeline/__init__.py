from .classifier import classify_question
from .prolog_generator import generate_prolog_facts
from .query_formulator import formulate_query
from .executor import execute_prolog_query
import json

def run_pipeline():
    with open("data/examples.json") as f:
        examples = json.load(f)

    for example in examples:
        print(f"\n--- Example: {example['id']} ---")

        classification = classify_question(example['context'], example['question'])
        print(f"Classification: {classification}")

        if classification == "logic":
            kb = generate_prolog_facts(example['context'])
            query = formulate_query(example['question'])
            result = execute_prolog_query(kb, query)
            print(f"Result: {result}")
        elif classification == "ranking":
            print("Ranking logic not implemented yet.")
        else:
            print("Unable to classify.")