class myNumber:
    def __init__(self, no1, no2):
        print("In init ")
        self.n1 = no1
        self.n2 = no2
    def set(self, no1,no2):
        self.n1 = no1
        self.n2 = no2
    def printNo(self):
        # print("Number 1 is : ", self.n1)
        # print("Number 2 is : ", self.n2)
        print("In print")
        print(self.n1,self.n2)
    # def get(self):
    #     return self.n1, self.n2
    
ob1=myNumber(10,20)
ob2=myNumber(12.36,56.78)
ob2.set(100,200)   
ob2.printNo()