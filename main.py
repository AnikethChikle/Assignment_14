from Classes import Circle, Rectangle, Triangle

if __name__ == "__main__":
    
    circle = Circle(5)
    print(f"Area of {circle.name}: {circle.area()}")
    print(f"Perimeter of {circle.name}: {circle.perimeter()}")

    rectangle = Rectangle(4, 6)
    print(f"Area of {rectangle.name}: {rectangle.area()}")
    print(f"Perimeter of {rectangle.name}: {rectangle.perimeter()}")

    triangle = Triangle(3, 4, 5, 5)
    print(f"Area of {triangle.name}: {triangle.area()}")
    print(f"Perimeter of {triangle.name}: {triangle.perimeter()}")