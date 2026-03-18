# exercise_1.py

name = "Hammad"
age = 25
drinks_coffee = True
salary = 75000.0

retirement_age = 60
cups_per_day = 3
price_per_cup = 150
days_per_week = 7

print(f"My name is {name}. I am {age} years old. Coffee drinker: {drinks_coffee}. My salary is Rs. {salary}.")

years_until_retirement = retirement_age - age

weekly_coffee_budget = cups_per_day * price_per_cup * days_per_week

print(f"Years until retirement: {years_until_retirement}")

if drinks_coffee:
    print(f"Weekly coffee budget: Rs. {weekly_coffee_budget}")
else:
    print("Weekly coffee budget: Rs. 0")