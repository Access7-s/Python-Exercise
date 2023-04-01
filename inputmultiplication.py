#program for multiplication table of entered number.
#prompt user for input
num=int(input("Enter a positive number: "))
#iterate the loop 10 times.
for i in range(1,11):
    print(f"{num} * {i} =",num*i)
