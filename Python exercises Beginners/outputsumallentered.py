'''a program to enter the numbers till the user wants and at
the end it should display the sum of all the numbers entered'''
print("Enter 0 to exit or  enter the number to sum")
num=(input("Enter the number : "))
summ=0
while num!="":
    summ=summ+int(num)
    num=(input("Enter another number : "))

print(f"The total sum of total number entered {summ}")
