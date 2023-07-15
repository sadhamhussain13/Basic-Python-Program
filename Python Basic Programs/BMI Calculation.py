# program to calculate BMI value

weight=int(input())
h1=float(input())
height=h1**2
bmi=weight/height
if bmi <= 18.5:
   print("Underweight")
elif bmi<=25:
   print("Normal")
elif bmi<=30:
   print("Overweight")
else:
   print("Obesity")