class C1:
    def process(self):
        print("Process in C1")


class C2:
    def process(self):
        print("Process in C2")


class C3(C1, C2):
    pass


obj = C3();
obj.process()
