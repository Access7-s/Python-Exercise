def status():
    crt=int(input("Enter the credits earneda: "))
    if crt>=90:
        print("Senior status")
    elif crt>=60:
        print("Junior status")
    elif crt>=30:
        print("Sophomere status")
    else:
        print("Freshman status0")

status()
