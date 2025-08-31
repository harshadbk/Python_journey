#  math modules

import math
import random
import datetime

a = 24
print(round(a,3))
print(math.ceil(a))

print(math.sqrt(a))

# Function	Description	Example
# math.sqrt(x)	Square root of x	math.sqrt(25) → 5.0
# math.pow(x, y)	x raised to power y	math.pow(2, 3) → 8.0
# math.exp(x)	Exponential e^x	math.exp(1) → 2.718...
# math.log(x, base)	Logarithm	math.log(100, 10) → 2.0
# math.floor(x)	Rounds down	math.floor(3.7) → 3
# math.ceil(x)	Rounds up	math.ceil(3.2) → 4
# math.fabs(x)	Absolute value	math.fabs(-5) → 5.0
# math.factorial(n)	Factorial	math.factorial(5) → 120
# math.gcd(x, y)	Greatest common divisor	math.gcd(8, 12) → 4
# math.degrees(x)	Radians to degrees	math.degrees(math.pi) → 180.0
# math.radians(x)	Degrees to radians	math.radians(180) → 3.14

# trignometry functions sin cos tan


#  random Module (Generating Random Numbers)


print(round(random.random(),1))

a = 10
b = 100

print(random.uniform(a,b))

print(random.randint(a,b))

print(random.randrange(a,b,3))

my_list = [1,2,5,4,7,8,9,9,10]

print(random.choice(my_list))

print(random.choices(my_list,k=4))

print(random.sample(my_list,9))

print(random.shuffle(my_list))
print(my_list)


# date time functions

print(datetime.datetime.now())

print(datetime.datetime.today())

year = 2024
month = 3
day = 24
print(datetime.date(year, month, day))

print(datetime.time(10,12,30))

print(datetime.datetime.strptime("2024-03-24","%Y-%m-%d"))

now.strftime("%d/%m/%Y") → '24/03/2024'

datetime.timedelta(days=5)

now = datetime.datetime.now()
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted_date)  # Output: 24-03-2024 14:30:15

from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=7)  # Add 7 days
past_date = now - timedelta(days=7)  # Subtract 7 days

print(future_date)  # Output: 2024-03-31
print(past_date)    # Output: 2024-03-17

