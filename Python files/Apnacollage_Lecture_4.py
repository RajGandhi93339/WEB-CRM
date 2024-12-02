# Dictionary in python
# dictory example
"""info = {
    "firstname": "",
    "middlename": "",
    "surname": "",
    "age": 1,
    "Marks": 1.50,
    "subject": ("python", "c", "java", ".net"),  # tuple
    "topics": [
        "chapter1",
        "topic1",
        "practice1",
        "chapeter2",
        "topics2",
        "practice2",
    ],  # list
}

print(type(info))
print(info["topics"])
info["class"] = "10"
print(info)"""

# nested dictionary
# dictionary k under dictory its called nested dictionary

student = {"name": "Khapara", "subjects": {"phy": 97, "chem": 98, "Science": 95}}

"""print(student)
print(student["subjects"]["chem"])
"""

# Dictionay metthods
# .keys methods
"""print(student.keys()) #return all keys
print(student["subjects"])"""

# type cast
"""print(list(student.keys()))

print(student.values())  # return all values

print(student.items()) #Return tuple forms 

print(list(student.items())) #Return tuple forms to list

print(student["name2"]) #return Error 
print(student.get("name2")) #return None value 


print(student["name"])
print(student.get("name"))"""

# Update dictionary methods
"""student.update({"City": "SURAT"})
print(student)

new_dic = {"State": "Gujarat", "Country": "India"}
student.update(new_dic)
print(student)
"""
# Sets in python
"""dictionaryExample = {"no1": "1", "no2": "2", "no3": "3", "no4": "4", "no5": "5"}
setexample = {1, 2, 3, 4, 5}
print(type(dictionaryExample))
print(type(setexample))"""

# Set ignore duplicate values
"""duplicatesetexample = {1, 2, 2, 3, 4, 4, 5, "hello", "world", "world"}
print(duplicatesetexample)"""

# create empty sets
"""ex1 = {}
ex2 = set()

print(type(ex1))
print(type(ex2))
"""
# Set methods
"""set.add()  # add an elements
set.remove()  # remove elements
set.clear()  # set empty or clear set data
set.pop()  # removes a random values
set.union(set2)  # combines both set values & return new
set.intersection(set2)  # combines common values & return new
"""

"""
setmethod = {1, 2, 3, 4, 5}
setmethod.add(6)
print(setmethod)

setmethod.remove(5)
print(setmethod)

# setmethod.clear()
# print(setmethod)

print(setmethod.pop())
print(setmethod.pop())

set1 = {1,1,2,3}
set2 = {"hi","raj",1,2}
set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)
"""
