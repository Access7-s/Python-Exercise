def grade():
    per=int(input("enter your percentage : "))
    if per>=70:
        print("Your Grede is A")
    elif per<69 and per>=60:
        print("Your grade is B")
    elif per<59 and per>=50:
        print("Your grade is C")
    else:
        print("You are fail")

grade()
