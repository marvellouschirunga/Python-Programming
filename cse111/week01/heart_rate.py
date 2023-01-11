"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

name = input("First and last name: " )
age = int(input("Your age: "))
max_heart_rate_per_minute = 220 - age
fastest_rate = (85/100) * max_heart_rate_per_minute
slowest_rate = (65/100) * max_heart_rate_per_minute
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {int(fastest_rate)} and {int(slowest_rate)} beats per minute.")

n = 2
c = 3
r = 1

p = 3 * n - (17*2**c) / (r+5)
d = 3 * n - 17 * c * c / (r+5)
t = 3 * n - (17 * c * c) / r + 5
print (p)
print(d)
print(t)