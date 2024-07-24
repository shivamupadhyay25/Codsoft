import string
import random
weak_password = string.ascii_lowercase
moderate_password = string.ascii_lowercase+string.ascii_uppercase+string.digits
strong_password = string.ascii_letters+string.digits+string.punctuation
while True:
    a = "PASSWORD GENERATOR"
    b = a.center(50,"-")
    print(b,"\n")
    print("1.Generate a new password")
    print("2.Exit")
    x = int(input("Enter your choice(1-2) : "))
    if x == 1:
        length = int(input("Please enter the length of password : "))
        print("select password complexity : ")
        print(" " + "1.Weak")
        print(" " + "2.Moderate")
        print(" " + "3.Strong")
        complexity_user = int(input("Enter your choice(1-3) : "))
        if complexity_user == 1:
            password = "".join(random.choices(weak_password,k=length))
            print("The generated password is : ")
            print(password,"\n")
            q = input("<--press Enter-->")
            continue
        elif complexity_user == 2:
            password1 = "".join(random.choices(moderate_password,k = length))
            print("The generated password is : ")
            print(password1,"\n")
            q = input("<--press enter-->")
            continue
        elif complexity_user == 3:
            password2 = "".join(random.choices(strong_password,k = length))
            print("The generated password is : ")
            print(password2,"\n")
            q = input("<--press enter-->")
            continue
        else:
            print("Invalid choice. Please try again")
            q = input("<--press enter-->")
            continue
    elif x == 2:
        print("Thanks for using")
        break
    else:
        print("Invalid choice. Please try again")
        q = input("<--press enter-->")
        continue