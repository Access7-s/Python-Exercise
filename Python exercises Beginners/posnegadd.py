def postneg():
    a=int(input("Enter postive oe negative integer: "))
    add=0
    while a != 0: 
        if a > 0:
            print("Type:Positive")
            add+=a
        elif a < 0:
            print("Type:Negative")
        a=int(input("Enter another number: "))

    return add

print(postneg())

        
        
    
    
