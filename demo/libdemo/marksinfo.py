data = "90,45, 66, 77  88;34"

import re

marks = re.findall(r"\d+", data)
marks = [int(v) for v in marks]

print("Total  : ", sum(marks))
print("Max    : ", max(marks))
print("Min    : ", min(marks))
print("Avg    : ", sum(marks) // len(marks))
