'''
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. 
On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.

Work as a team to write a Python program named discount.py that gets a customer’s subtotal as input and gets the current day 
of the week from your computer’s operating system. Your program must not ask the user to enter the day of the week. Instead, 
it must get the day of the week from your computer’s operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. Your 
program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the 
discount amount if applicable, the sales tax amount, and the total amount due.
'''

from datetime import datetime

subtotal = float((input("Enter Subtotal: " )))
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

if (subtotal >= 50) and (day_of_week == 1 or 2):
    discount = subtotal - (subtotal - (0.1 * subtotal))
else:
    print()

sales_tax = (0.06 * subtotal)
total_amount_due = subtotal + sales_tax
print(f"Discount amount is: ${discount:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total amount due is: ${total_amount_due:.2f}")


