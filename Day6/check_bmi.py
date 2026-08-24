height = float(input("Enter your height :"))
weight = float(input("Enter your weight :"))

try:
    bmi = weight // (height * height)
except Exception:
    print("height cannot be zero")
else:
    print("Your BMI is",bmi)
finally:
    print("Successfully executed code")