def max(a,b,c):
    """This function takes three numbers as input and outputs the
        largest of the three numbers """
    if a>b and a>c:
        print(f"{a} is maximum")
    elif b>a and b>c:
        print(f"{b} is maximum")
    else:
        print(f"{c} is maximum")
        
n1=int(input("Enter 1st number "))
n2=int(input("Enter 2nd number"))
n3=int(input("Enter 3rd number"))
max(n1,n2,n3)
