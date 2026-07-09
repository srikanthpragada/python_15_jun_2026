class Course:
    def __init__(self, title, duration=24, fee=0):
        # Object Attributes
        self.title = title
        self.duration = duration
        self.fee = fee

    def to_dict(self) -> dict:
        return {"title" : self.title,
                "duration" : self.duration,
                "fee" : self.fee,
                "netfee" : self.fee * 1.12}

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



