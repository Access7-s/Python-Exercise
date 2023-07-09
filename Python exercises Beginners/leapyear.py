def leap():
    yr=int(input("enter the year you want to check :"))
    cal=yr%4
    if cal==0:
        print(f"{yr} year is a leap year: ")
    else:
        print(f"{yr} year is not a leap year: ")

leap()
