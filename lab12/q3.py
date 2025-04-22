class Solid:
    def __init__(self):
        pass
    def surfaceArea(self):
        pass
    def volume(self):
        pass
class Cube:
    def __init__(self,side):
        self.side=side
    def surfaceArea(self):
        return 6*self.side*self.side
    def volume(self):
        return (self.side)**3
class Cuboid:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def surfaceArea(self):
        return 2*((self.l*self.b)+(self.b*self.h)+(self.h*self.l))
    def volume(self):
        return self.l*self.b*self.h
solid=Cube(5)
print(solid.volume(),solid.surfaceArea())
solid=Cuboid(5,6,7)
print(solid.volume(),solid.surfaceArea())