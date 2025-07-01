import json

with open("grouped_result.json", "r", encoding="utf-8") as f:
    grouped = json.load(f)

flattened = []
for entry in grouped:
    age = entry["age"]
    gender = entry["gender"]
    for item in entry["items"]:
        item_flat = {
            "age": age,
            "gender": gender,
            "category": item["category"],
            "name": item["name"],
            "reason": item["reason"]
        }
        flattened.append(item_flat)

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(flattened, f, ensure_ascii=False, indent=2)
