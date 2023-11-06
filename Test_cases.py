# A test file that contains unit tests for the shape classes
import unittest
from  Classes import Circle, Rectangle, Triangle

# A test class for the circle class
class TestCircle(unittest.TestCase):
    def setUp(self):
       
        self.circle = Circle(5) # A circle object with radius 5

    def test_name(self):

         self.assertEqual(self.circle.name, "circle")

    def test_area(self):
        
        self.assertAlmostEqual(self.circle.area(), 78.5)

    def test_perimeter(self):

       self.assertAlmostEqual(self.circle.perimeter(), 31.4)

# A test class for the rectangle class
class TestRectangle(unittest.TestCase):
    def setUp(self):
      
        self.rectangle = Rectangle(10, 20) 

    def test_name(self):
        
        self.assertEqual(self.rectangle.name, "rectangle")

    def test_area(self):
       
        self.assertEqual(self.rectangle.area(), 200)

    def test_perimeter(self):
        
        self.assertEqual(self.rectangle.perimeter(), 60)

# A test class for the triangle class
class TestTriangle(unittest.TestCase):
    def setUp(self):
       
        self.triangle = Triangle(15, 12, 9, 10) 

    def test_name(self):

        self.assertEqual(self.triangle.name, "triangle")

    def test_area(self):

         self.assertEqual(self.triangle.area(), 90)

    def test_perimeter(self):
        
        self.assertEqual(self.triangle.perimeter(), 34)

if __name__ == "__main__":
    unittest.main()
