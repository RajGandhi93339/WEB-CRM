# Loops in python
# Loops are used to repeat instructions.
#  While loop
"""i = 1
while i <= 5:
    print(i)
    i += 1

j = 5
while j >= 1:
    print(j)
    j -= 1
"""

# break and countinue

"""i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
    print("Finish 1")

i = 1
while i <= 5:
    print(i)
    if i == 3:
        i += 1
        continue

    print("Finish 2")
"""

# For loop

"""nums = [1,2,3,4,5]

for value in nums:
    print(value)

t1 = ("Apnacollage","hi","Raaj")

for data in t1:
    print(data)

str = "Apnacollage"

for char in str:
    print(char)
"""

# for else
"""
str = "Apnacollage"

for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("END")
"""
# renge

# seq = range(5) #renge define

"""for i in range(5): #range stop
    print(i)

for i in range(2,5): #range (start,stop)
    print(i)

for i in range(1,100,2): #range (start,stop,step)
    print(i)
"""
# Pass statement

"""for i in range(5): #range stop
    pass
"""