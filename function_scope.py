def sum(a, b):
    #a and b are local variables
    c=a+b
    z=3 #it creates a local variable z which is distroyed after function returns 
    return c

z=8 #this is a global variable 
print(sum(2,3))
print(z)
