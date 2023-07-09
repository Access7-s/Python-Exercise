def divison():
    a=int(input("a:"))
    b=int(input("b:"))
    try:
        result=a/b
        print(result)
    except ZeroDivisionError:
        print("Error: Cant devide by zero")
        
divison()
    
