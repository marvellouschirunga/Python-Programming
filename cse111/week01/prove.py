'''
Many companies wish to understand the needs and wants of their customers more deeply so the company can create products
that fill those needs and wants. One way to understand customers more deeply is to record the values entered by 
customers while they are using a program and then to analyse those values. One common way to record values is for a program 
to store them in a file.
'''


import math
from datetime import datetime
'''
width = int(input("Enter the width of the tire in millimeters: "))
aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
diameter = int(input("Enter the diameter of the wheel in inches: "))

volume = (math.pi * (width * width) * aspect_ratio * ((width * aspect_ratio) + (2540 * diameter))) / 10000000000

print(f"The approximate volume of the tire is: {volume:.2f} liters")
'''
#current_date_and_time = datetime.now()
current_date = datetime.now()
day_of_week = current_date.weekday()

print(f"{current_date:%Y-%m-%d}")
