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

    @property
    def currentvalue(self):
        return self.value

c1 = Counter(100)  # Create an object of Counter class
# print(c1.value)
c1.increment()
c1.increment(10)

print(c1.currentvalue)  # using property
c2 = Counter()



