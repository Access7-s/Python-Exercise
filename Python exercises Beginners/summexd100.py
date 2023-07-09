''' a program that sums a series of (positive) integers entered by the user, excluding all numbers
that are Greater than 100.'''
summ = 0
while True:
    n = int(input("Enter a positive integer (enter 0 to stop): "))
    if n == 0:
        break
    elif n > 100:
        print("Number is greater than 100, excluding it!")
        continue
    else:
        summ += n
print("The sum of all positive integers less than or equal to 100 is:", summ)
