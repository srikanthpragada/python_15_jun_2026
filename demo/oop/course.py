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


print(Course.gettaxrate())

c  = Course("Gen AI", 24, 10000)
print(c.get_net_fee())

c2  = Course("PowerBI", fee = 8000)
c2.set_duration(20)
c2.show()

print(c2.__dict__)



