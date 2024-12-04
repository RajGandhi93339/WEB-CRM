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

'''n = 1
def Evenodd(n):
    if n % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

number = int(input("check number is Even or Odd :"))

Evenodd(number)'''