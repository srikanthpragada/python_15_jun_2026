
def operation(x, y, task):
    print(task(x, y))

def inc(num):
    return num + 1

def add(a, b):
    return a + b


operation(10, 20, add)
#operation(10, 20, inc)
