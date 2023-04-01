def percentage(a,b):
    '''The function determines the percentage ofworking days and determines the eligibility of a person to sit in exams'''
    percntg=(((a-b)/a)*100)
    f_percent=f"{percntg:.2f}"
    return f_percent

ttlwd=int(input("Enter the total number of working days: "))
ttlad=int(input("Enter the total number of absent days: "))
result=(percentage(ttlwd,ttlad))
print("you were present",result,"percentage of total working days")
print(result)
n=type(result)
print(n)
if result < "80":
    print("You are not eligible to sit in exam")
else:
    print("You are eligible to sit in exam")

       

