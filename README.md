# Logic-LLM Reimplementation

This is an original reimplementation of the Logic-LLM architecture described in the [Logic-LM paper](https://arxiv.org/abs/2210.03629). This version mimics the key components:

- LLM-based classification of logic questions
- Logic translation into Prolog
- Constraint solving using LLM
- Symbolic reasoning with Prolog (via PySwip)

## How to Run

1. Add your OpenAI API key to your environment (`export OPENAI_API_KEY=...`)
2. Run the main pipeline:

```bash
python main.py
