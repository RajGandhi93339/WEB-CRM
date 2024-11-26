# List in python

"""marks1 = 12
marks2 = 24
marks3 = 45
marks4 = 77
"""
"""marks = [12, 24, 45, 77]
print(marks)
print(type(marks))  # <class 'list'>
print(len(marks))
print(marks[0])
print(marks[1])

marks.append(5)  # Value enter in list
print(marks)
print(marks.sort())  # Sort in ascending order
print(marks)
print(marks.sort(reverse=True))  # Sort in reverse order descending
print(marks)
print(marks.reverse())
print(marks)

name = ["b", "d", "f", "c", "e" ,"a"]
print(name.sort())
print(name)
print(name.reverse()) #Sort in reverse order
print(name) 
name.insert(1,"Raj") #Insert value in list or list[1]
print(name)
"""
# list Methods

"""list = [2, 4, 1, 5, 9, 1, 6, 7]
list.remove(1)  # Remove value in index
print(list)
list.pop(4) #remove value particular index
print(list)"""

# tuple - brother of list
# tuple is immutable
# list is mutable
# List using []
# tuple using () //Single values with , its called tuple
"""
tup = (2, 1, 3, 1)
print(tup[0])
print(tup[1])
print(type(tup))

tup1 = 1
tup2 = 1.5
tup3 = "hello"
tup4 = ("hi",)
print(type(tup1))  # //type int
print(type(tup2))  # //type float
print(type(tup3))  # //type string
print(type(tup4))  # //type tuple
"""
# tuple methods

tup = (1, 2, 3, 4)
print(tup[1:3])

# index method
tup1 = (2, 4, 1, 3, 1)
print(tup1.index(1))  # first element position in tuple //output 2

# count method
print(tup1.count(4))  # element count in tuple
