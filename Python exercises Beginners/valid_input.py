valid_input = False
while not valid_input:
    age = int(input("Enter your age :"))
    if age <0 :
        print("Invalid input. Age cannot be negative")
    else:
        valid_input= True

print(f"Your age is {age}.")
