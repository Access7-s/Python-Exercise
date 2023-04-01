"""a program to print Fibonacci series of n terms where n is input by user:  """
n=int(input("Enter the number :"))
n1=0
n2=1
count=0
#checking if the number is valid for fibonacci
if n<0:
    print("Please enter positive number: ")
elif n==1:
    print("The fibonacci sequence upto",n,":")
    print (n1)
else:
    print("Fibonacci sequence:")
    while count< n:
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count= count+1
        

    
