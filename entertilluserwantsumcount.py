'''a program to enter the numbers till the user wants and at the end
it should display the count of positive, negative and zeros entered.'''
print("For Exiting the program enter blank value i.e'Enter button' ")
num=int(input("Enter the number: "))
sum=0
posnum=0
negnum=0
zeronum=0
while num!="":
    if (int(num))>0:
        posnum=posnum+1
        sum=sum+(int(num))
    elif (int(num))<0:
        negnum=negnum+1
        sum=sum+(int(num))
    else:
        zeronum=zeronum+1
    num=(input("Enter the number: "))
print(f"the total sum is {sum} and the total positive, negative and zero enetered are {posnum}, {negnum}, {zeronum} respextively.")
        

