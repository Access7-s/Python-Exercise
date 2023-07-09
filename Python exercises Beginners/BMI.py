def bmi():
    wt=int(input("Enter your weight in kilograms : "))
    ht=int(input("Enter your height in centimeters: "))
    BMI=(wt/(ht/100)**2)
    f_BMI="{:.2f}".format(BMI)
    if BMI<18.5:
        print(f"You are underweight as your BMI is {f_BMI}.")
    elif BMI>=18.5 and BMI<25:
        print(f"Your BMI is {f_BMI} and you are normal weight.")
    elif BMI>=25 and BMI<30:
        print(f"Youy are overweight as your BMI is {f_BMI}.")
    elif BMI>=30:
        print(f"You are obese as your BMI is {f_BMI}. ")
bmi()
    
