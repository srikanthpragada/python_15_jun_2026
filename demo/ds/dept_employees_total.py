data = [('IT', 'James', 100000),
        ('IT', 'Martin', 140000),
        ('SA', 'Jack', 80000),
        ('FI', 'Dave', 90000),
        ('FI', 'Scott', 130000)]


depts = {}
for emp in data:
     dept, name, salary = emp
     dept_data = depts.get(dept, ([], 0))
     dept_data[0].append(name)
     total = dept_data[1] + salary
     depts[dept]  = (dept_data[0], total)

for deptname, details in depts.items():
    names = ",".join(details[0])
    print(f"{deptname:5} {names:30} {details[1]}")



