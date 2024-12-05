#WAP to create a new file "practice.txt" using python. add the following data in it :

'''with open("Python files\practice.txt","w") as r:
    r.write("hi everyone \n")
    r.write("we are learning file i/o using java.\n")
    r.write("i like programming in java.")'''

#wap that replace all occurrences of "java" with "python" in above file.

with open("Python files\practice.txt","r") as f:
    data = f.read()
    print(data)

    newdata=data.replace("java","python")
    print(newdata)