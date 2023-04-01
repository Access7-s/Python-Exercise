import datetime
def grade(a,b):
    '''The function is defined to take input from user and convert and calculate it to total percentage of class attended'''
    per_attend=((a-b)/a)*100
    return per_attend

twd=int(input("ENter total number of working days :"))
tad=int(input("enter total number of adsent days :"))    
year=int(input("enter the year of completion :"))
mon= int(input("enter the months of completion :"))
day=int(input("enter the day of completion :"))
time= datetime.datetime(year,mon,day)
pert= grade(twd,tad)
res=print(f"The total you attended the class is {pert:.2f}% of whole working session.")
print(f"{res} in {time}")
if pert < 80:
    print("you will not be able to sit the exam")
else:
    print("you are eligible to sit in exam")

