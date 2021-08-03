dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 
'poodle', 'collie']

for breed in dog_breeds:
  print(breed)
#############################################################
def spaces():
    print("----------------------------------------------------------------------------- \n \n \n-----------------------------------------------------------------------------")
def minispace(a):
    if a == 1:
      print("------------  OVER HERE  ---------  RIGHT HERE ------------- THIS WAY --------------")
    print( "--------------------------------")
##################
spaces()
##################
promise = "I will not chew gum in class"

for x in range(5):
  print(promise)

#####################
spaces()
#####################

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

######################
minispace(2)
#####################
#CONTINUE
# the continue keyword move the index to the next value
# in the list, without 
# executing the code in the rest of the for loop
# example : drinking age is 21
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print (i)

######################
minispace(2)
######################
# using while loop , you are adding students to a Poetry class
# the size is capped at 6
# use .pop() to take a student and add it to the poetry class

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  
print(students_in_poetry)

#########################
spaces()
#########################
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
    
print(scoops_sold)


######################
minispace(2)
#####################
# LIST COMPREHENSIONS

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

#######################
minispace(2)
#######################
#this is exactly the same as the one above
heights1 = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster1 =[]

for height1 in heights1:
    if height1 > 161 :
        can_ride_coaster1.append(height1)
print(can_ride_coaster1)

#######################
spaces()
#######################
#other example
celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp*(9/5) + 32 for temp in celsius]

print(fahrenheit)

##############################
minispace(2)
##############################
#REVIEW
single_digits = range(10)
squares = []

for item in single_digits:
  print(item)
  squares.append(item**2)
  
cubes = [item**3 for item in single_digits]
print(cubes)

################################
minispace(2)
################################
# simple example
numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    continue
  print(number)

minispace(2)

numbers = [2, 4, 6, 8]
for number in numbers:
  print("hello!")

minispace(2)

# using BREAK , the difference with continue is it'll stop the program
numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    break
  print(number)

minispace(2)

for i in range(3):
    print(i)

minispace(2)

for i in range(3):
    print(5)

minispace(2)

def whatever(i):
    #or just write it here (i = 1)
    while i <= 10:
        print(i)
        i+=1
    return ("last number that wasnt printed is "+ str(i))
    #if there is no return above, it will output "none" in the last line
print(whatever(1))

minispace(2)

my_list = [5, 10, -2, 8, 20]
desired_list = [10, 8, 20]
# to create my_list equal to the desired 
x =[i for i in my_list if i >5]
print(x)

################################################
spaces()
################################################
# Return the count of how many numbers in the list are divisible by 10
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count


print(divisible_by_ten([20, 25, 30, 35, 40]))

##################
minispace(2)
##################
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list

print(add_greetings(["Owen", "Max", "Sophie"]))


####################
minispace(2)
####################
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

########################
minispace(2)
########################
def odd_indices(lst):
  empty_list = []
  
  for x in lst :
    if x%2 != 0:
      empty_list.append(x)
    
  return empty_list
    
print(odd_indices([4, 3, 7, 10, 11, -2]))

###########################
minispace(1)
###########################

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

##############################
minispace(2)
################################

def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))

###################################
minispace(2)
##################################

def larger_sum(lst1,lst2):
  y= 0
  for x in lst2:
    y += x
  
  return y
  
print(larger_sum([1, 9, 5], [2, 3, 7]))

############################
minispace(2)
############################
# return list whose elements sum is greater , if its equals, return lst1
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))

#############################
minispace(2)
#############################

def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))


#####################################
spaces()
#####################################
# function return the largest number in "nums"

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

print(max_num([50, -10, 0, 75, 20]))

#########################
minispace(2)
###########################
# the function should return a list of the indices where the values were equal in lst1 and lst2

def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


#############################
minispace(2)
#############################
# the function should return True if lst1 is the same as lst 2 reversed. The function should return False otherwise
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

