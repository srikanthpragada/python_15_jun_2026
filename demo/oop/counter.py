class Counter:
    # Constructor
    def __init__(self, start = 0):
        # Object Attributes
        self.value = start

    # Method
    def increment(self, step = 1):
        self.value += step

    def decrement(self, step = 1):
        self.value -= step

    def get_value(self):
        return self.value

c1 = Counter(100)  # Create an object of Counter class
# print(c1.value)
c1.increment()
c1.increment(10)

print(c1.get_value())
c2 = Counter()



