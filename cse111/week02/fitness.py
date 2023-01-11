# Equations
# (women)  bmr = 447.593 + 9.247 weight + 3.098 height − 4.330 age
# (men)  bmr = 88.362 + 13.397 weight + 4.799 height − 5.677 age


## G = gender W = Weight H = Height
g = input('What is your Gender: Put F for female and M for male ')
w = float(input('What is your Weight in pounds? '))
a = int(input('What is your age? '))
bday = input('What is your birthday in the format /(YYYY-MM-DD):  ')
h = float(input('What is your height? '))
wk = w *0.45359237 
hcm = h * 2.54

if  g.lower() == 'm':
    gender = "male"
    bmr = 88.362 + (13.397 * wk) + (4.799 * hcm) - (5.677 * a)

elif g.lower() == 'f':
     gender = "female"
     bmr = 447.593 + (9.247 * wk) + (3.098 * hcm) - (4.330 * a)

print(f'''Gender is {gender} 
Body mass index is: {bmr}
Age = {a}
Birthday = {bday}
Your weight in kilograms {wk}
Your height in cm {hcm}''')
