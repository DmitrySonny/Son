class Shape():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return 'Shape {}*{}'.format(self.width, self.height)

class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__vertex_number = 3

    def area(self):
        return self.width * self.height / 2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__vertex_number = 4

    def area(self):
        return self.width * self.height
