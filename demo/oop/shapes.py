class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        super().show()
        print(self.width, self.height)

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def show(self):
        super().show()
        print(self.side)

    def area(self):
        return self.side * self.side


s = Square(100, 200, 50)
s.show()
print(s.area())

