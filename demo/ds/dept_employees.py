data = [('IT', 'James', 100000),
        ('IT', 'Martin', 140000),
        ('SA', 'Jack', 80000),
        ('FI', 'Dave', 90000),
        ('FI', 'Scott', 130000)]


depts = {}
for emp in data:
     dept, name, salary = emp
     employees = depts.get(dept,[])
     employees.append(name)
     depts[dept]  = employees

print(depts)


