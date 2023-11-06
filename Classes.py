# A parent class that represents a geometric shape
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        
        raise NotImplementedError("Subclass must implement this method")

    def perimeter(self):
        
        raise NotImplementedError("Subclass must implement this method")

# A subclass that represents a circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        
        return 3.14 * self.radius ** 2

    def perimeter(self):

         return 2 * 3.14 * self.radius

# A subclass that represents a rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("rectangle")
        self.length = length
        self.width = width

    def area(self):
        
        return self.length * self.width

    def perimeter(self):
        
        return 2 * (self.length + self.width)

# A subclass that represents a triangle
class Triangle(Shape):
    def __init__(self, base, height, side1, side2):
        super().__init__("triangle")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
       
        return 0.5 * self.base * self.height

    def perimeter(self):
        
        return self.base + self.side1 + self.side2
