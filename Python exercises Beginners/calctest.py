def calculator():
    user=input("Enter your user name: ")
    passs=input("Enter your password: ")
    if user=="admin" and passs=="admin":
        a=int(input("Enter a number : "))
        b=int(input("Enter another number : "))
        print("Please select any operations among thses\n1.C for calculator\n2. A for  Average of numbers\n3. E for Exit.")
        c=input("Enter Your choice:")
        if c=="C":
            print("Enter + for sum, - for substract, * for multiplication, / for division")
            calc=input("enter your choice")
            if calc=="+":
                result=a+b
                print(result)
            elif calc=="-":
                result=a-b
                print(result)
            elif calc=="*":
                result=a*b
            elif calc=="/":
                result=a/b
                print(result)
        elif c=="A":
            result=((a+b)/2)
            print(result)
        elif c=="E":
            print("YOu exited. Thank you")
    else:
        print("Invalid crediantials")

calculator()
        
                        
