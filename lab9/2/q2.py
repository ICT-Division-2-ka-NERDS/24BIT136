def q2():
    def binary_eqi(n:int):
        if n == 0:
            return
        binary_eqi(n // 2)
        print(n % 2, end='')

    num = int(input("Enter a positive integer: "))

    if num == 0:
        print("0")
    else:
        binary_eqi(num)

q2()