'''a program that uses a loop to add up all the even numbers between
100 and 200, inclusive using break and continue functions'''
summ=0
n=100
valid=True
while (valid):
    if n>201:
        break
    elif n%2==0:
        summ+=n
    n+=1
print(f"The sum of even numbers between 100 and 200 is: {summ}")

        
        
        
    
