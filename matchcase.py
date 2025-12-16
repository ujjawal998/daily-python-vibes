a=int(input("enter a number:"))
match a:
    case 1:
        print("you won 100$")
    case 4:
         print("you won 50$")
    case 7:
        print("you won 10$")
    case _:
        print("better luck next time")