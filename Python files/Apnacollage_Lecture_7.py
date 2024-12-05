# file i/o in python
# python can be used to perform operation on a file.
"""
f = open("D:\WEB CRM\Python files\demo.txt","a+") #open("file path",MODE)
f.write("\nappend java")
f.close()


'r' open for reading (default)
'w' open for writing , truncating the file first
'x' create a new file and open it for writing
'a' open for writing , append the text to the end
'b' binary mode
't' text mode
'+' open a disk file for updating..
"""
# with using

with open("D:\WEB CRM\Python files\demo.txt", "w") as f:
    data = f.write("JAVA FILE")
    print(data)

# deleting a file
'''import os

os.remove("D:\WEB CRM\Python files\demo.txt")
'''