height = float(input("Enter the height in meters: ")) #Take input height in float from the user 
weight = float(input("Enter the weight in kilograms: ")) #Take input weight in float from the user 

bmi = weight / (height ** 2) #Calculate the BMI using this formula 

if bmi >= 30: #Checking the conditions using IF-ELIF statements
    print("Obesity") #Print Obesity if bmi is greater than or equal to 30
elif bmi >= 25 and bmi < 29: #Checks the second condition using ELIF Statement
    print("Overweight") #Print Overweight if bmi is greater than or equal to 25 and less than 29
elif bmi >= 18.5 and bmi < 25: #Checks the third condition using ELIF Statement
    print("Normal") #Print Normal if bmi is greater than or equal to 18.5 and less than 25
elif bmi < 18.5: #Checks the fourth condition using ELIF Statement
    print("Underweight") #Print Underweight if bmi is less than 18.5
