from pyswip import Prolog

def execute_prolog_query(facts, query):
    prolog = Prolog()
    for line in facts.strip().splitlines():
        cleaned = line.strip().rstrip('.')
        if not cleaned or len(cleaned.split('(')) < 2:
            print(f"Skipping invalid Prolog line: {repr(cleaned)}")
            continue
        try:
            prolog.assertz(cleaned)
        except Exception as e:
            print(f"Failed to assert fact: {cleaned}")
            print(e)
            continue

    try:
        cleaned_query = query.strip().lstrip("?-").rstrip(".").strip()
        result = list(prolog.query(cleaned_query + "."))
        return "A" if result else "C"
    except Exception as e:
        print(f"Failed to run query: {query}")
        print(e)
        return "C"

