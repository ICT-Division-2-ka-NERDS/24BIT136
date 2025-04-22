class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real, imag)

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"
    
c1 = ComplexNumber(8, 6)    
c2 = ComplexNumber(-98, -30)  

print("First Complex Number is : ", c1)
print("Second Complex Number is :", c2)
print("Addition is :", c1 + c2)
print("Subtraction is :", c1 - c2)
print("Multiplication is :", c1 * c2)
print("Division is :", c1 / c2)