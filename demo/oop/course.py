class Course:
    # Class attribute or static attribute
    taxrate = 12

    @staticmethod
    def gettaxrate():
        return Course.taxrate


    def __init__(self, title, duration = 24, fee = 0):
        # Object Attributes
        self.title = title
        self.duration = duration
        self.fee = fee

    def show(self):
        print(f"Title: {self.title}, Duration: {self.duration}, Fee: {self.fee}")

    def get_net_fee(self):
        return self.fee + self.fee * Course.taxrate / 100

    def get_title(self):
        return self.title

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def __gt__(self, other):
        print('__gt__')
        return self.fee > other.fee

    def __str__(self):
        return f"Title: {self.title}, Duration: {self.duration}, Fee: {self.fee}"


# print(Course.gettaxrate())
#
# c  = Course("Gen AI", 24, 10000)
# print(c.get_net_fee())
#
# c2  = Course("PowerBI", fee = 8000)
# c2.set_duration(20)
# c2.show()
#
# print(c2.__dict__)

courses = [Course('Java', 36, 8000),
           Course('C', 30, 5000),
           Course("DS", 30, 10000)
           ]

for course in sorted(courses):
    print(course)





