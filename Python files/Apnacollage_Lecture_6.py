# Functions in PYTHON
"""
def cal_Sum(i,j):
    sum = i + j
    print(sum)
    return sum

i = 10
j = 12
cal_Sum(i,j) 

cal_Sum(25,25)

cal_Sum(50,50)

cal_Sum(2,3)
"""
# Recursion in Python
# when a functions call itself countinues or repeatedly.
"""
n = 5
def show(n):
    if n == 0:
        return
    print(n)
    show(n - 1)  # Recursive function
    print("END")

show(10)
"""
# Recursion factorial example
n = 4

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

print(fact(n))
