'''
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
Write a Python program named boxes.py that asks the user for two integers:
1. the number of manufactured items
2. the number of items that the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. 
Note that the last box may be packed with fewer items than the other boxes.
'''

import math

items_manufactured = int(input("Enter number of items manufactured: "))
items_to_pack = int(input("Enter number of items user will pack per box: "))

boxes_needed = math.ceil(items_manufactured / items_to_pack)
print(f"For {items_manufactured} items, packing {items_to_pack} items in each box, you will need {boxes_needed} boxes.")