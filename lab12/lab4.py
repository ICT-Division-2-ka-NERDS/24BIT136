class myComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def printC(self):
        print(self.real,"+",self.imag,"j")
    def __add__(self, c2): #operator overloading
        print("In __add__")
        ob3= myComplex(0, 0)
        ob3.real = self.real + c2.real
        ob3.imag = self.imag + c2.imag
        return ob3
    def addC(self, c2): #not operator overloading
        ob3= myComplex(0, 0)
        ob3.real = self.real + c2.real
        ob3.imag = self.imag + c2.imag
        return ob3
ob1 = myComplex(1, 2)
ob2 = myComplex(3, 4)
ob3 = myComplex(0, 0)
ob1.printC()
ob2.printC()    
ob3=ob1.addC(ob2) 
ob4= ob1 + ob2
ob3.printC() 
#h.W. = sub, mul, div 