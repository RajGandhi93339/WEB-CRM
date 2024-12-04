# WAP print numbers from 1 to 100

"""
i = 1
while i <= 100:
    print(i)
    i += 1
"""

# print numbers from 100 to 1.
"""
j = 100
while j >= 1:
    print(j)
    j -= 1
"""

# print the multiplication table of a number n.
"""
n = int(input("Enter the number of multiplication table :"))
i = 1
while i <= 10:
    print(n*i)
    i += 1
"""
# WAP print the elements of the following list using a loop:
#  [1,4,9,16,25,36,49,64,81,100]

"""i = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0
while index < len(i):
    print(i[index])
    index += 1
"""
# Wap for a number x in this tuple using loop:
"""
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
x = 36
while i < len(num):
    if x == num[i]:
        print("Found at index :",i)
        break
    else:
        print("finding...")
    i += 1
"""
# Modulo example using while loop
"""
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
"""
# WAP print the elements of the following list using a for loop:
# [1,4,9,16,25,36,49,64,81,100]

i = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''for num in i:
    print(num)
'''
# WAP print the elements of the following list using a loop:
#  [1,4,9,16,25,36,49,64,81,100]
i = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 64
for value in i:
    if value == x:
        print("found value", x)
        break
    else:
        print(value)
