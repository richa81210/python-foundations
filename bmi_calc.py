height = float(input("What is your height in cm? "))
weight = float(input("What is your weight in kg? "))

#Convert height to meters

# 1 metre = 100 cm
# ? = x cm
#x/100 m

height_in_metres = height/100

def bmi(x, y):
    bmi_var = x/(y**2)
    print(f"BMI is {bmi_var:.2f}")
    if bmi_var < 18.5:
        category = "underweight"
    elif bmi_var>18.5 and bmi_var<24.9:
        category = "normal weight"
    elif bmi_var> 25 and bmi_var<29.9:
        category = "over weight"
    elif bmi_var>=30:
        category = "obese"
    print(f"You are {category}")

bmi(weight, height_in_metres)