n=int(input("a:"))
m=int(input("b:"))
try:
    result=n/m
except ZeroDivisionError :
    print ("Error: cant divide by zero")
else:
    print(f"{n} / {m} is {result}")

    
