a=int(input("Enter a:"))
b=int(input("Enter b:"))
valid=False
while not valid:
    try:
        numerator=a
        denominator=b

        result=numerator/denominator
        print(result)
        valid=True
    except ZeroDivisionError:
        print("Error:Denominator cannot be 0.")

        
