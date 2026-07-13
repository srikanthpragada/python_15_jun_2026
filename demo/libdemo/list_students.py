import re
f = open("students.txt", "rt")
students = {}

for line in f:
    line = line.strip()
    # look for email address in the line
    em = re.search(r"[a-zA-Z0-9_]+@[a-zA-Z0-9]+", line)
    if em is None:
        continue

    # look for marks in the line at the end
    mm = re.search(r"\d+$", line)
    if mm is None:
       continue

    students[em.group(0)] = int(mm.group(0))

for name, marks in students.items():
    print(f"{name:15}  {marks:3}")



