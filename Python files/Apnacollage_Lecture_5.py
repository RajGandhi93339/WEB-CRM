# Loops in python
# Loops are used to repeat instructions.
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

i = 1
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
        continue
    i += 1
    print("Finish 2")
