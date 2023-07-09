def leap(n):
    yr=n%4
    if yr==0:
        print('It is Leap year')
    else:
        print("It is not a leap year")

thyr=int(input('enter year:'))
print(leap(thyr))

def sp(mp,d):
    pp=mp-d
    return pp
p1=int(input("enter marked price :"))
p2=int(input("enter discounted amount:"))
print(f"the net amount to pay is {sp(p1,p2)}")


def grade(n):
    if n>=70:
        print("You got garde A")
    elif n<70 and n>=60:
         print("You got grade B")
    elif n<60 and n>=50:
         print("You got grade C")
    else:
         print("You failed and your grade is F")
         
pctg=int(input("enter your percentage"))
grade(pctg)

def places():
    print("Kathmandu = PAshupatinath Temple")
def tourist(city):
    if city=="kathmandu":
        print(city, "Pashupati Temple")
    elif city=="pokhara":
        print("Fewa lake")
    elif city=="nepalgunj":
        print("Bageshwori Temple")
    elif city=="birgunj":
        print("Birgunj Ghanta Ghar")
    else:
        print("No data available, Sorry for inconvienence.")
places()   
place=input("Enter the city name :",)
tourist(place)
