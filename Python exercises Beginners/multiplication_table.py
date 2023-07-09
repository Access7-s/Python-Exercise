def multiplication_table(digit):
    
    for i in range(digit+1):
        print(f"{i:02d}", end= " ")
    for j in range(1,digit+1):
        print(f"{(i)*j:02d}", end=" ") 

multiplication_table(10)

