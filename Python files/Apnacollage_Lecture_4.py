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
"""print(list(student.keys()))"""

"""print(student.values())  # return all values

print(student.items()) #Return tuple forms 

print(list(student.items())) #Return tuple forms to list

print(student["name2"]) #return Error 
print(student.get("name2")) #return None value 
"""

print(student["name"])
print(student.get("name"))

# Update dictionary methods
student.update({"City": "SURAT"})
print(student)

new_dic = {"State": "Gujarat", "Country": "India"}
student.update(new_dic)
print(student)
