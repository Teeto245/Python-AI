first_name =  "Kaniz"

second_name = "Nuzhat"

second_name

last_name = 'Kamal'
last_name
#whether you use double quotes or single quote it'll work

total = 140 + 3

print(total)

print(second_name+ " "+ last_name)

print(len(first_name))
print(len(second_name))
print(len(last_name))

name_of_boy = 'bob'
print(len(name_of_boy))


# Direct assignment
is_ready = True

# From comparisons
age = 18
can_vote = age >= 18  # True

score = 75
passed = score > 60   # True

age = 25

# Equality
print(age == 25)     # True - equals
print(age != 30)     # True - not equals

# Greater/Less than
print(age > 20)      # True - greater than
print(age < 30)      # True - less than
print(age >= 25)     # True - greater or equal
print(age <= 25)     # True - less or equal

name = 'Kamal'

print(name =='Kamal')

print(name != "Kamal")


cr = 130
cg = 2.5
can_grd = cr >= 130 and cg >= 2.00
print(can_grd)

name_2 = "Kaniz Nuzhat"

string = f"Hello {name_2}! Welcome to Kcafe!"

print(string)

text = "Python ProgrAmming"

print(text.lower())      # "python programming"
print(text.upper())      # "PYTHON PROGRAMMING"
print(text.title())      # "Python Programming"

text2 = "HURRAh yeey"

print("lower case: " + text2.lower())
print("upper case: " + text2.upper())
print("title case: " + text2.title())

temperature = 16

if(temperature > 25):
  print("It's so hot!")
elif temperature > 10:
  print("it's medium, not hot but chilly")
else:
  print("COOL")

score = 15

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")


is_rich = False
grade = 3
if is_rich:
   if grade >= 3.7:
      print("kitty party allowed")
   else:
      print("just simple discussion")
else:
   print("only high hello")
   


is_programmer = True
age = 15
if is_programmer:
   
   if age>=18:
      print(f"person whose age is {age}"+" can fly to abroad for cs role")
   elif age>=13:
      print(f"person whose age is {age}"+" wait till 18")
   else:
      print(f"person whose age is {age}"+" is a baby and a programmer in fiction")
else:
   print("not a programmer")


print("hello")
print("hello")
print("hello")
print("hello")


for i in range(4):
   print("hello")

# Count from 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

for i in range(5):
   print("hurrah")

name = "Kaniz Nuzhat Kamal"
for letter in name:
   print(letter)

colors = ["red", "green", "blue"]

for color in colors:
   print(f"i like {color}")

heros = ["srk", "ranbir", "salman"]

for hero in heros:
   print(f"I like to watch {hero} movies")


count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1  # Increase count by 1

# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4
i = 0
while i<=5:
   print(i)
   i=i+1
# use while when you want the loop to 
# to work as long as the condition is true

for i in range(0,6):
   print(i)

# use for loop when iterating over a range

# CREATING LISTS 1.EMPTY LIST 2.LIST WITH ITEMS

items = []

food_items = ["banana", "pasta", "coke"]

for i in food_items:
   print(i)
# Accessing items , index -1 means last theke 
# first er ta

print(food_items[-3])

# lists are mutable

food_items[0] = 'raspberry'

print(food_items)

food_items.append("dark chocolate")
print(food_items)

food_items.insert(1, "chips")
print(food_items)

food_items.remove("chips")
print(food_items)

last = food_items.pop()
print(last)

food_items.insert(1, "berry")
print(food_items)

print(food_items[-1])

del food_items[0]
print(food_items)

myname = ['k', 'a', 'n', 'z']
print(myname)
myname.insert(3, 'i')
print(myname)

del myname[4]
print(myname)

myname.pop()
print(myname)
myname.append("Z")
print(myname)

myname.insert(3, 'i')
print(myname)

numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))         # 6 (length)
print(numbers.count(1))     # 2 (count occurrences)
print(numbers.index(4))     # 2 (find position)

# Sorting
numbers.sort()              # Sort in place
print(numbers)              # [1, 1, 3, 4, 5, 9]

numbers.reverse()           # Reverse order
print(numbers)              # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()   # Create a copy

print(len(myname))
print(myname.count('Z'))
print(myname.index('Z')) 

# methods like copy, len, count, index, sort
# methods like reverse
fish = ['Tuna', 'Tuna', 'Hilsha', 'Prawn','Rui']
print(len(fish)) # len method worked on the list 
#now we want to do count,index to return how many
# times something occurred in the list and in which
# index it happened.
print(fish.count('Tuna'))     # 2 (count occurrences)
print(fish.index('Tuna'))     # 2 (find position)

mylist1 = ['kangaroo', 'kiwi', 'olives', 'cherry']

mylist2 = mylist1.copy()

#print(mylist1)
print(mylist2)

mylist2.insert(0,'hotdog')

mylist1 = mylist2.copy()

print(mylist1)

# Check if list is empty
fruits = []
if fruits:
    print("List has items")
else:
    print("List is empty")