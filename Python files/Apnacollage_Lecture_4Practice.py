# WAP Store following word meanings in a python disctionary :
# table : "A piece of furniture","list of facts & figures"
# cat : "a small animal"

"""dict = {
    "table": ["A piece of furniture", "list of facts & figures"],
    "cat": "a small animal",
}
print(dict)"""

# WAP to you are given a list of subjects for students. assume
# one classroom is required for 1 subject. how many classrooms are needed
# by all students.

"""setsubject = {
    "python",
    "java",
    "c++",
    "python",
    "javascript",
    "java",
    "python",
    "java",
    "c++",
    "c",
}
print(type(setsubject))
print(setsubject)
print("Total classroom is :",len(setsubject))
"""

# WAP to enter marks of 3 subjects from the user and
# store them in dictionary. start with an
# empty dictionary & add one by one.
# use subject name as key & marks as value.

"""markdic = {}

m1=int(input("Enter marks of maths :"))
m2=int(input("Enter marks of English :"))
m3=int(input("Enter marks of Science :"))

markdic.update({"MATHS":m1,"English":m2,"Science":m3})
print(markdic)
"""

# figure out a way to store 9 & 9.0 as separate values in the set.
# (you can take help of built-in data types)

store = {("int", "9"), ("string", "9.0")}
print(store)
