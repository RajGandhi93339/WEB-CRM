# WAF to print the length of a list(list is the parameter)
"""
list = [1,2,3,4,5]
def Fun_lengthofList(list):
    print(len(list))

#WAF to print the elements of a list in a single line
def print_list(list):
    for item in list:
        print(item,end=" ")

Fun_lengthofList(list)
print_list(list)
"""
# WAF to find the factorial of n.

"""n = 1
def factNumbers(n):
    sum = 1
    for item in range(1,n+1):
        sum *= item
    print(sum)

value = int(input("enter number for factorial :"))

factNumbers(value)
"""
# WAF to COnvert USD to INR.
"""
US = 1

def ConvertRS(US):
    inr = 81.24
    convert = US * inr
    print("INR",convert)

USD = int(input("enter USD to convert INR :"))

ConvertRS(USD)
"""
# WAF enter the number to find even or odd.

"""n = 1
def Evenodd(n):
    if n % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

number = int(input("check number is Even or Odd :"))

Evenodd(number)"""

# recursion practice

# WAP a recursive function to calculate the sum of first n natural numbers.
"""n=5
def calc_sum(n):
    if(n == 0 ):
        return 0
    return calc_sum(n-1) + n

print(calc_sum(10))
"""
# WAP a recursive function to print all elements in a list.
"""
n = [1,2,3,4,5,"Hello"]

def printelements(n):
    for items in n:
        print(items)
    else:
        return 0

printelements(n)
"""
fruits = ["apple", "banana", "litchi", "mango"]


def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx + 1)


print_list(fruits)

