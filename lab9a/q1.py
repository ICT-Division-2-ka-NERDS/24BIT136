def fun():
    print("This is empty function named 'fun' ")
    
def disp():
    print("This is empty function named 'disp' ")
    
def msg():
    print("This is empty function named 'msg' ")
    
lst=[fun, disp, msg]
for i in lst:
    i()