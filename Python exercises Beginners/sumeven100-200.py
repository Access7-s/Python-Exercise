"""a program that uses a loop to add up all the even numbers between 100 and 200, inclusive. 
"""
sum_even = 0
for i in range(100, 201):
    if i % 2 == 0:
        sum_even += i
print("The sum of even numbers between 100 and 200 is:", sum_even)
