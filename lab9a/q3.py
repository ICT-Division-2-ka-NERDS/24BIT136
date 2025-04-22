import random
l=[]
for i in range(0,10):
    l.append(random.randint(-15, 15))

t=list(map(lambda x:x**2,l))
print(l,t)
