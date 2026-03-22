import json

data = ["What is AI?", "Explain entropy"]

results = []

for prompt in data:
    # fake LLM call (replace later)
    response = f"Answer to: {prompt}"
    results.append({"prompt": prompt, "response": response})

with open("results/output.json", "w") as f:
    json.dump(results, f, indent=2)
