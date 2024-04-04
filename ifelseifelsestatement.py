num1=int(input("Enter the first"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
num4=int(input("Enter the fourth number"))

if num1>num2 and num1>num3 and num1>num4:
    print(f"{num1} is greater than {num2},{num3} and {num4}")
elif num2>num1 and num2>num3 and num2>num4:
    print(f"{num2} is greater than {num1},{num3},{num4}")
elif num3>num1 and num3>num2 and num3>num4:
    print(f"{num3} is greater than {num2},{num1},{num3}")
elif num4>num1 and num4>num2 and num4>num3:
    print(f"{num4} is greater than {num1},{num2},{num3}")


    # Calculate BMI
bmi = weight/ (height ** 2)

# Classify BMI
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

    # display the result
print(f"Your BMI is {bmi:2f}, and your category is {category}")

