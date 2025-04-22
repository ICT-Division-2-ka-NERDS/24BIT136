class myNumber:
    def set(self, no1,no2):
        self.n1 = no1
        self.n2 = no2
    def printNo(self):
        # print("Number 1 is : ", self.n1)
        # print("Number 2 is : ", self.n2)
        print("In print")
        print(self.n1,self.n2)
    def get(self):
        return self.n1, self.n2

ob1 = myNumber()
ob2 = myNumber()

ob1.set(10,20)
ob2.set(30.51,40.42)

ob1.printNo()
ob2.printNo()

print(ob1.get())
a,b= ob2.get()
print("a is =",a,"b is =",b)
