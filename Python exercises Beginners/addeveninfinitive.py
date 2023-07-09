'''a program that solves (a) but this time using an infinite loop, break and continue
statements.'''
summ = 0
i = 100
while True:
    if i > 200:
        break
    if i % 2 == 0:
        summ += i
    i += 1
print("The sum of even numbers between 100 and 200 is:", summ)
