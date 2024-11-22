import time
import selenium.webdriver

choose = bool(input("You want new order True/False:"))
print(type(choose))
name = input("Enter your name : ")
city = input("Enter your city : ")
age = input("Enter your age : ")
# print("U want order option : /n YES/NO : ", input(Passkey))
# print("Calculate price :", price)

# Arithmetic operators
a = 5
b = 2

Sum = a + b
print(sum)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)  # remainder
print(a**b)  # a^b = 5^2 = 25

# relational operator / comparison operator

a = 50
b = 20
print(a == b)  # false
print(a != b)  # True
print(a > b)  # True
print(a >= b)  # True
print(a < b)  # false
print(a <= b)  # True

# Assignment operators
num = 10
# num = num + 10
# num += 10
# num -= 10
# num *= 10
# num /= 10
# num %= 10
num **= 10

print("Num :", num)

# logical operators
# (Not, and , or)
a = 50
b = 20
print(not (a > b))
print(not False)
print(not True)

val1 = True
val2 = False
print("AnD operator:", val1 and val2)
print("Or operator:", val1 or val2)

# type conversion
a = 2
b = 2.50
sum = a + b
print(sum)
