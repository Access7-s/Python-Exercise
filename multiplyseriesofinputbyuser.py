'''The following while loop is meant to multiply a series of integers input
by the user, until a sentinel value of 0 is entered'''
product=1
#Explicit conversion of variable
num= int(input("Enter first number: "))
while num!=0:
    product= product*num
    print("product=", product)
    #promting user for new value of num
    num=int(input("Enter the number to be multiplied : "))
    
    
    
