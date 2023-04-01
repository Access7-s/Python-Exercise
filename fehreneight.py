def ST(a,b,c):
    sum=a+b+c
    if a==b or b==c or a==c:
        sum=0

    return sum
n1=int(input("enter n1 :"))
n2=int(input("neterr n2:"))
n3=int(input("enter n3 :"))
result=ST(n1,n2,n3)
print(result)
print("the numbers are {} {} {} ".format(n1,n2,n3))

