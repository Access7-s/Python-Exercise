def prosum(x,y):
    if x<0 or y<0:
        calc=0
    else:
        calc=x*y
    return calc
a=int(input("Enter a number: "))
b=int(input("Enter 2nd number: "))
result=prosum(a,b)
print(f"The required result is {result}")
