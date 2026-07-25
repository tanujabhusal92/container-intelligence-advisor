import json
from collections import Counter


registries = Counter()
images = Counter()
instructions = Counter()


with open(
    "dataset/output/train.jsonl"
) as f:

    for line in f:

        data = json.loads(line)

        output = data["output"]

        for item in output.split("\n"):

            if item.startswith("Recommended Registry"):
                registries[
                    item.split(":")[1].strip()
                ] += 1

            if item.startswith("Recommended Image"):
                images[
                    item.split(":")[1].strip()
                ] += 1


print("\nRegistry Distribution")
print(registries)

print("\nImage Distribution")
print(images)
