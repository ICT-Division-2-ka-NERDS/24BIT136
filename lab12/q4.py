class Shape:
    def __init__(self):
        pass
    def perimeter():
        pass
class Circle:
    def __init__(self,radius):
        self.r=radius
    def perimeter(self):
        return 2*3.14*self.r
class Square:
    def __init__(self,side):
        self.side=side
    def perimeter(self):
        return 4*self.side
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
class EquilateralTriangle:
    def __init__(self,side):
        self.side=side
    def perimeter(self):
        return 3*self.side
Shape=Circle(5)
print("Circle perimeter:",Shape.perimeter())
Shape=Square(4)
print("Square perimeter:",Shape.perimeter())
Shape=Rectangle(4,5)
print("Rectangle perimeter:",Shape.perimeter())
Shape=EquilateralTriangle(3)
print("Equilateral Triangle perimeter:",Shape.perimeter())
