import json
import os

os.makedirs("results", exist_ok=True)

with open("results/output.json") as f:
    data = json.load(f)

n_prompts = len(data)
total_chars = sum(len(item["response"]) for item in data)
avg_chars = total_chars / n_prompts if n_prompts else 0

with open("results/metrics.txt", "w") as f:
    f.write(f"n_prompts={n_prompts}\n")
    f.write(f"total_chars={total_chars}\n")
    f.write(f"avg_chars={avg_chars:.2f}\n")

print("Evaluation complete.")
print(f"n_prompts={n_prompts}, total_chars={total_chars}, avg_chars={avg_chars:.2f}")