#Conditional statement
#if_elif_else

'''light = "none"
if light == "red":
    print("Stop")
elif light == "Green":
    print("Go")
elif light == "Yellow":
    print("wait")
else:
    (print("light is not working"))

print("program is stop")'''

# Grade student based on marks
stdname = input("ENTER STUDENT NAME :")
marks = int(input("ENTER MARKS :"))

# Std1 = "akash"
# marks1 = "92"

# Std2 = "Harsh"
# marks2 = "84"

# Std3 = "akash"
# marks3 = "74"

# Std5 = "Kevin"
# marks4 = "55"

if(marks >= 90):
    print("A Grade")
elif(marks >= 80):
    print("B Grade")
elif(marks >= 70):
    print("C Grade")
elif(marks >= 60):
    print("D Grade")
else:print("Not eligible for next grade....")