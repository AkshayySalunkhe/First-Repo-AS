def fib(n):

    num1 = int(input("Enter a\n"))
    num2 = int(input("Enter b\n"))
    if num1 == 1:
        print(num1)
    else:
        print(num1)
        print(num2)
    for i in range(2,n):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num3)
fib(10)#put here those number of lines upto which you want to print fibonacci series.
