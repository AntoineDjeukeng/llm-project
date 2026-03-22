import json

with open("results/output.json") as f:
    data = json.load(f)

score = sum(len(d["response"]) for d in data)

with open("results/metrics.txt", "w") as f:
    f.write(f"score={score}")
