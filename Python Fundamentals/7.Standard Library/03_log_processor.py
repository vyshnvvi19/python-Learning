import re
from collections import Counter
from pathlib import Path

file = Path(__file__).parent / "app.log"

text = file.read_text(encoding="utf-8")

levels = re.findall(r"\b(INFO|WARNING|ERROR)\b", text)

count = Counter(levels)

print("Log Summary")
print("-----------")
print("INFO:", count["INFO"])
print("WARNING:", count["WARNING"])
print("ERROR:", count["ERROR"])
