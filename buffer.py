import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print(c)
print("Area:", c.area())
print("Circumference:", c.circumference())