class Students:
    def __init__(self, name, enrollment_no,marks1,marks2):
        print("In init ")
        self.n1 = name
        self.n2 = enrollment_no
        self.m1 = marks1
        self.m2 = marks2
    # def set(self, name, enrollment_no,marks1,marks2):
    #     self.n1 = name
    #     self.n2 = enrollment_no
    #     self.m1 = marks1
    #     self.m2 = marks2
    def printNo(self):
        # print("Number 1 is : ", self.n1)
        # print("Number 2 is : ", self.n2)
        print("In print")
        return (self.n1,self.n2,self.m1,self.m2)
    # def get(self):  
    #     return self.n1, self.n2, self.m1, self.m2 
    def cal_avg(self):
        return (self.m1+self.m2)/2
  

ob1=Students("Rudra", "24BIT136", 90, 95)
ob1.printNo()
ob1.cal_avg()

ob2=Students("krish", "24BIT120", 85, 90)
ob1.printNo()
ob2.cal_avg() 
