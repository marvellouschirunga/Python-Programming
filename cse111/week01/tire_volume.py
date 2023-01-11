'''
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. The volume of space 
inside a tire can be approximated with this formula:


v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
'''

'''
Many companies wish to understand the needs and wants of their customers more deeply so the company can create products
that fill those needs and wants. One way to understand customers more deeply is to record the values entered by 
customers while they are using a program and then to analyse those values. One common way to record values is for a program 
to store them in a file.
'''

import math
from datetime import datetime

phone_number = 0
width = int(input("Enter the width of the tire in millimeters: "))
aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
diameter = int(input("Enter the diameter of the wheel in inches: "))

volume = (math.pi * (width * width) * aspect_ratio * ((width * aspect_ratio) + (2540 * diameter))) / 10000000000

if width >= 180 and aspect_ratio >= 60 and diameter >= 15:
    tire_price  = 120
elif width > 90 and aspect_ratio > 30 and diameter == 7:
    tire_price = 70
else:
    tire_price = 30


print(f"The approximate volume of the tire is: {volume:.2f} liters")
print(f"Tire Price is: ${tire_price}")
ans = input("Do you want to make this purchase? (Y/N)")
if ans[0] == "Y" or ans[0] == "y" :  
    phone_number = input("Please provide us with your phone number: ")
else:
    print("Thank you for enquiring with us")

current_date = datetime.now()
with open("volume.txt","at") as volumes_file:
    print(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, Customer Phone Number: {phone_number}", file=volumes_file)
    

