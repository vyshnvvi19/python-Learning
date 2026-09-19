import json
from pathlib import Path

file = Path("sample.json")

data = json.loads(file.read_text(encoding="utf-8"))

for student in data:
    student["name"] = student["name"].upper()

output = Path("updated_students.json")

output.write_text(
    json.dumps(data, indent=4),
    encoding="utf-8"
)

print("JSON file transformed successfully.")