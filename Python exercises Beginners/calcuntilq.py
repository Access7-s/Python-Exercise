menu='''
Select an operation to perform on two numbers

"+" to add
"-" to substract
"*" to multiply
"/" to divide
"q" to quit

Please enter your chooice :'''

choices=["+","-","*","/","q"]
calc=input(menu).lower()

while (calc!="q"):
    if calc in choices:
        a=int(input("Enter no.1 : "))
        b=int(input("Enter no.2 : "))
        if calc=="+":
            sum=a+b
            print(f" The sum : {sum}")
        elif calc=="-":
            diff=a-b
            pirnt(f"The difference : {diff}")
        elif calc=="*":
            mul=a*b
            print(f"The product : {mul}")
        elif calc=="/":
            divs=a/b
            print(f"The division : {divs}")
    else:
        print("\nInvalid option")

    calc=input(menu).lower()
    
