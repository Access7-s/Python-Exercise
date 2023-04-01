temperature=int(input("Enter the temperature of today's : "))
humidity=int(input("Enter the hiumidity of todays : "))
if temperature >= 85 and humidity > 60:
    print("muggy day taday")
elif temperature >=85:
    print("warm, but not muggy today")
elif temperature >=65:
    print("pleasant today")
elif temperature >=45:
    print("Cold today")
else:
    print("Very cold today")
