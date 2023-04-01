def sum2(a,b):
    summ=a+b
    if summ>15 and summ<20:
        suum=20
    else:
        suum=summ
    return suum
n1=int(input("Enter the first number: "))
n2=int(input("Enter the 2nd number: "))
Sum=sum2(n1,n2)
print(f'The required sum is {Sum}')
