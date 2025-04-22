import math 
def func(n):
        return n*n
lst=[5,10,15,20]
m1=map(math.radians, lst)
m2=map(math.factorial, lst)
m3=map(func, lst)
print(set(m1))
print(tuple(m2))
print(list(m3))

def func2(n,m):
    return n*m
lst2=[1,2,3,4,5]
m4=map(func2,lst,lst2)
print(tuple(m4))

def divby7(n):
    return True if n%7 == 0 else False

lst1=['A','a','P','56','R','t','4','+']
f1=filter(str.isalpha,lst1)
print(list(f1))

lst2=[14,222,5,63,5,8,55,4]
f2=filter(divby7,lst2)
print(list(f2))