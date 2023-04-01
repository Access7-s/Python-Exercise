import random
num=random.randint(1,21)
for i in range(5):
    guess=int(input("Enter your guess no.(betweem 1 and 20) : "))
    if guess==num:
        print(f"YOu have guessed the correct number i.e {guess}")
        break
    elif guess>num:
        print("Your guess was high, guess lower values")
    elif guess<num:
        print("Your guess was low, guess higher values")

print(f"The correct answer was {num}")

        
