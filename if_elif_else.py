age=int(input("enter your age:"))
if(age>18):
    print("drive allowed")
elif(age==18):
    print("lets schedule a interview")
elif(age==0):
    print("invalid age")
else:
    print("drive not allowed")
    