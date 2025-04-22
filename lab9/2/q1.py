def q1():
    list = []  
    def prime_Factors(n: int, i=2):
        if n <= 1:  
            print(list)
            return
        while n % i == 0:
            list.append(i)
            n //= i  
        prime_Factors(n, i + 1)  

    num = int(input("Enter a number: "))  
    prime_Factors(num)

q1()