class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


def print_area(shape):
    print("Area:", shape.area())


rectangle = Rectangle(4, 5)
circle = Circle(3.5)

print_area(rectangle)  # Saída: Area: 20
print_area(circle)     # Saída: Area: 38.465
