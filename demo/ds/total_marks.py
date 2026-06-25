data = [(1, 90),  (1, 59), (3, 87), (3, 60), (4, 90), (2, 88)]

students = {}

for rollno, marks in data:
    total = students.get(rollno, 0)
    total += marks
    students[rollno] = total

for rollno, total in sorted(students.items()):
    print(rollno, total)




