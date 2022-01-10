def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)
print(fact(4))  # you can put those number here whose factorial you want to calculate