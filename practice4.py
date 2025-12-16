a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
operation=input("enter operation +,-,*,/")
match operation:
    case "+":
        print("addition",a+b)
    case "-":
        print("subtraction",a-b)
    case "*":
        print("multiplication",a*b)
    case "/":
        print("division",a/b)
  
        