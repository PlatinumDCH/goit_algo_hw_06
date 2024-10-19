import math

class Form:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(Form):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Form):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
class Triangle(Form):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.heigth = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_area(self):
        return 0.5 * self.base * self.heigth
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
    