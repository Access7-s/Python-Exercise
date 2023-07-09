'''a program to find the smallest digit in a number entered by the user
using a loop.'''

num=(input("Enter the number: "))
digit="9"
for i in num:
    if i<digit:
        digit=i
print("The smallest digit in the prrogram is :",digit)
    
