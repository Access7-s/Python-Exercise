"""a program to print a pattern of numbers like below using a loop:

1
22
333
4444
55555
"""
n=int(input("Enter the numbers of rows: "))

for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()
