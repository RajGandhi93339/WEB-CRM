# WAP to create a new file "practice.txt" using python. add the following data in it :

"""with open("Python files\practice.txt","w") as r:
    r.write("hi everyone \n")
    r.write("we are learning file i/o using java.\n")
    r.write("i like programming in java.")"""

# wap that replace all occurrences of "java" with "python" in above file.

# with open("Python files\practice.txt","r") as f:
#     data = f.read()
#     print(data)

#     newdata=data.replace("java","python")
#     print(newdata)

# with open("Python files\practice.txt","w") as f:
#     f.write(newdata)

# search if the word "learning" exists in the file or not.
"""word = "python"
with open("Python files\practice.txt", "r") as f:
    data = f.read()
    finddata = data.find(word)
    if finddata != -1:
        print("found")
    else:
        print("not found")"""

# WAP to find in which line of the file does the word "learning" occure first.
# print -1 if word not found.
"""def findline():
    word = "kamlesh"
    data = True
    line_no = 1
    with open("Python files\practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)

            line_no += 1
    return -1


findline()
"""
count = 1
with open("Python files\practice.txt", "r") as f:
    data = f.read()
    print(data)
    num = data.split(",")
    for val in num:
        if int(val)%2 == 0:
            count += 1
    print(count)
           
