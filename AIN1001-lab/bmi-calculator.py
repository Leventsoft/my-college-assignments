weight = int(input("What's your weight in kilograms?\n"))
height = float(input("What's your height in meters?\n"))

bmi = weight / (height * height)

if bmi < 20:
    print("You are thin.")

elif 20 <= bmi and bmi < 25:
    print ("You are ordinary weighted.")

elif 25 <= bmi and bmi < 40:
    print ("You are obese")

elif bmi >= 40:
    print ("You have morbid obesity.")