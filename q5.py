"""
Create a classes Rectangle, Circle and Box and add respective attributes eg.: radius, length, width, height
for Rectangle, create methods to find out:
    perimeter
    area
    length of diagonal
for Circle, create methods to find out:
    circumference
    area
    diameter
for Box, create methods to find out:
    surface area
    volume
"""

class Rectangle:
    def __init__(self,length,breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
    def area(self):
        return self.length * self.breadth

    def diagonal_length(self):
        return (self.breadth**2 * self.height**2)**0.5

PI = 3.1415
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def circumference(self):
        return 2*PI*self.radius
    
    def area(self):
        return PI*(self.radius**2)
    
    def diameter(self):
        return 2*self.radius

class Box:
    def __init__(self,length,breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def surface_area(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height)

    def volume(self):
        return self.length * self.breadth + self.height

rect1 = Rectangle(4,8,10)
print("Area of rectangle:", rect1.area())
print("Perimeter of rectangle:", rect1.perimeter())
print("Length of diagonal:", rect1.diagonal_length())
print()

circle = Circle(4)
print("Area of Circle:", circle.area())
print("Perimeter of Circle:", circle.circumference())
print("Diameter of Circle:", circle.diameter())
print()

b1 = Box(2, 3, 5)
print("Surface Area of a Box:", b1.surface_area())
print("Volume of a Box:",b1.volume())
print()
