#dictionary creation

person = {}

person = {
  "name": "Kaniz",
  "age": 16,
  "hobbies": "art"
}

person

#get values by key

print(person['name'])
print(person['age'])

print(person['hobbies'])

# Add or update

person['job'] = 'doctor'

print(person)

person['gmail'] = 'abcd@gmail.com'
# get the values using the keys
print(person['gmail'])

print(person['age'])


def greet():
  print("HELLO KANIZ THE GORU")


greet()

def routine():
  day = 'Monday'
  if day == 'Friday':
    print("Today is holiday")
  else:
    print(f"you have school because today is {day}")

routine()


def calculate_price(price, discount, tax):

    discount_amount = price * discount / 100
    price_after_discount = price - discount_amount

    tax_amount = price_after_discount * tax / 100
    final_price = price_after_discount + tax_amount

    print("Final price:", final_price)


calculate_price(1000, 10, 5)


def daam_atlast(price, tax, discount):

  discount_amount = price * (discount/100)

  price_afterdisc = price - discount_amount

  after_tax = price_afterdisc * (tax/100)
  final_price = after_tax + price_afterdisc

  print("final price:", final_price)

daam_atlast(2000, 2, 50)

def calculate_area(length, width):

  area = length*width

  return area

area_create = calculate_area(2, 3)

print(f"Area is {area_create} sq ft")


def eat_eggs(day, no_of_eggs):

  return day*no_of_eggs

total = eat_eggs(3, 2)

print(f"No of eggs you have eaten are: {total}")


def make_projects(day, no_of_proj):

  return day*no_of_proj

pro = make_projects(3, 3)

print(f"We made {pro} projects this time.")


def subtraction(big, small):

  result = big - small
  print(f"Subtraction of {big}-{small}: {result}")
 
subtraction(1000, 70)


def multiplication(a,b):

  result = a * b

  print(f"Multiply {a} and {b} to get {result}")


multiplication(a = 70, b = 10)

def plus_num(a, b):

  result = a + b
  
  print(f"{a}+{b} = {result}")

plus_num(a = 39, b = 10)

def simple_function():

  numbers = [1, 2, 3, 4, 5]

  first_num = numbers[0]
  last_num = numbers[-1]

  return first_num, last_num

f,l = simple_function()

print(f"first number: {f} and last number: {l}")

# Import entire module
import random
for i in range(5):
# Use module functions
 number = random.randint(200, 250)
 choice = random.choice(['a', 'b', 'c', 'd', 'e', 'f','g'])
 print(number)
 print(choice)


import random

number2 = random.randint(100, 102)
print(number2)

choice = random.choice(["giraff","bunny","cow","kangaroo"])

print(choice)

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)
import requests

# Coordinates for Dhaka
#latitude = 23.81
#longitude = 90.41
# Coordinates for Sylhet
latitude = 24.90
longitude = 91.87
# Build the API URL
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)

# Convert the response into Python data
data = response.json()

#print(data)

temp = data['current']['temperature_2m']
print(temp)


import datetime

today = datetime.date.today()

print(today)