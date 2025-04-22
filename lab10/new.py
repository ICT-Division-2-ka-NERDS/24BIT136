def try2():
    try:
        a = int(input("Enter an integer"))
        b = int(input("Enter another integer"))
        c = a / b
        print ("Division = ", c)
    except ZeroDivisionError:
        print ("Division by zero error")    
try2()