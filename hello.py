def spaces(p):
    print("\n----------------------------------------------------- \n#"+str(p))
# parameters
# the special of the day will not always be mandarin oranges, 
# it will change every day. What if we wanted to call these 
# three statements again, except with a variable special? We can use parameters,
# which are variables that you can pass into the function when you call it

def greet_customer(special_item):
    print("Welcome to Engrossing Grocers.")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")

greet_customer("peanut butter")








###############################################
spaces(1)
###############################################
def mult_x_add_y(number,x,y):
  print(number*x + y)
  
mult_x_add_y(1,3,1)


#def greet_customer(special_item="bananas", grocery_store): 
# # this is not valid
    
#def greet_customer(special_item, grocery_store="Engrossing Grocers"): 
# # this is valid







################################################
spaces(2)
##################################################

# Returns
# functions can also return a value to the user so this value can be 
# modified or use later, when there is a result from a function 
# that can be stored in a variable,
# then its called a returned function value

def divide_by_four(input_number):
    return input_number/4

result = divide_by_four(16)
# result now holds 4
print("16 divided by 4 is " + str(result) + "!")
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")











#######################################################
spaces(3)
#######################################################
#you can also do this
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
  
my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)
print("I am "+str(my_age)+" years old and my dad is "+str(dads_age)+" years old")

##########################################################
spaces(4)
########################################################
def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2

x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)

spaces(5)
#here's another one
def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit

low, high = get_boundaries(100, 20)

print("Low limit: "+str(low)+", high limit: "+str(high))




########################################################
spaces(6)
########################################################
#Variables defined outside the scope/inside of a function may be accessible inside the body of the function 
# but not the other way around

header_string = "Our special is " 

def create_special_string(special_item):
    return header_string + special_item + "."
print(create_special_string("grapes"))

print (create_special_string("not grape"))

spaces(7)
#other example
current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age

print(current_year)

print(calculate_age(1970))

spaces(8)
#other example
def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)

print(song)

#########################################3
spaces(9)
#######################################
def average(num1,num2):
  return (num1+num2)/2
  
print(average(1, 100))
####################################
def square_root(num):
  return num**(1/2)

print(square_root(16))

###########################################
def tip(total,percentage): 
  return total*percentage/100

print(tip(10, 25))
#############################################
spaces(10)
###########################################
def win_percentage(wins,losses):
  return wins*(wins+losses)
print(win_percentage(5, 5))
print(win_percentage(10, 0))
print(win_percentage(7,3))
#############################################
def first_three_multiples(num):
  x= num*3
  print (num,num*2,x)
  return x


#############################################
spaces(11)
###########################################

def dog_years(name, age):
  return name+", you are "+str(age*7)+" years old in dog years"


print(dog_years("Lola", 16))
print(dog_years("Baby", 0))


#############################################
spaces(12)
###########################################

#remainder function :
def remainder(num1, num2):
  return (2*num1)%(num2/2)

print(remainder(15, 14))
print(remainder(9, 6))

#############################################
spaces(13)
#########################################
#dont know what this is for but..
my_baby_bool = "true"

print(type(my_baby_bool))

my_baby_bool_two = True

print(type(my_baby_bool_two))

############################################
def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"
  if user_name == "Robert":
    return "Well hello there!"

  
user_name = "Mike"

print(dave_check(user_name))
###############################################
spaces(14)
##############################################

def greater_than(x,y):
  if (x>y):
    return x
  if (y>x):
    return y
  if (y==x):
    return "These numbers are the same"
##############################################
#another one, remember to print the return
def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
  
print(graduation_reqs(120))
#################################################3
def graduation_reqs1(gpa, credits):
  if gpa >= 2.0 and (credits >= 120):
    return "You meet the requirements to graduate!"
print(graduation_reqs1(3.7,149))

############################################

def graduation_reqs3(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"
    #or -->  else: return "You do not meet either requirement for graduation."


#######################################################
spaces(15)
#########################################################
def thank_you(donation):
  if donation >= 1000:
    print("Thank you for your donation! You have achieved platinum donation status!")
  elif donation >= 500: 
    print("Thank you for your donation! You have achieved gold donation status!")
  elif donation >= 100:
    print("Thank you for your donation! You have achieved silver donation status!")
  else:
    print("Thank you for your donation! You have achieved bronze donation status!")

# what would happen if all of the "elif" statements were simply "if" statemen
# if you donated $1000, then the first three messages would all print
# also this

def grade_converter(gpa):
  if gpa >= 4.0 :
    return "A"
  elif gpa >= 3.0 :
    return "B"
  elif gpa >= 2.0 :
    return "C"
  elif gpa >= 1.0 :
    return "D"
  elif gpa >= 0.0 :
    return "F"

######################################
def raises_value_error():
  raise ValueError
  
try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")

############################################
def applicant_selector(gpa, ps_score, ec_count):
  if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
    return "This applicant should be accepted."
  elif gpa >= 3.0 and ps_score >= 90 and ec_count < 3:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."


##########################################
spaces(16)
#########################################

# LISTS

#lists of lists
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64],["Vik",68]]

ages = [["Aaron",15],["Dhruti",16]]

##########################################################################################
#ZIP

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names,dogs_names)
print(names_and_dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

###########################################################
spaces(17)
#Append

orders = ['daisies', 'periwinkle']
print (orders)

orders.append("tulips")
orders.append("roses")

print(orders)
######################################  
#other example
orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

new_orders = orders + ["lilac", "iris"]

broken_prices = [5, 3, 4, 5, 4] + [4]

###########################################
spaces(18)
############################################
#RANGE
my_range3 = range(1, 100, 10)  # ( START , END , JUMPS ) 
print (my_range3)
print(list(my_range3))

#other
list1 = range(5, 15, 3)

list2 = range(0,40,5)

print(list(list1)  +  list(list2))

######################################################

first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []
age.append(42)
all_ages = age + [32, 41, 29]
name_and_age = zip(first_names, all_ages)
ids = range(4)

############################################
spaces(19)
##################################################

list1 = range(2, 20, 3)

list1_len = len(list1)
print (list1_len)

#####################################################
# -1 is for the last element(what ever it is)
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']

print(len(shopping_list))
last_element= shopping_list[-1]

element5 = shopping_list[5]

print (element5 + last_element)
#########################################################
#other example
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]

print(beginning)

middle = suitcase[2:4]
print(middle)
#######################################################
# other example 


suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
end = suitcase[4:]
print(start, end)



#########################################################
spaces(20)
########################################################
#COUNT how much x is in y

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie',
 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count("Jake")
print (jake_votes)

#################################################
#SORT 
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
print(names)
# sort does not return anything, also "names" has been changed

##############################################
#SORTED
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)
print (games )
print( games_sorted)

# sorted didnt change "games"

################################################
spaces(21)
###################################################
#review
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser',
 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)  
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count('twin bed')
inventory.sort()


############################################################
spaces(22)
############################################################
#a function that return a new list where all elments are the same as in "lst"
# except for the element at "index", which should be double the value of the element
# at index of "lst"
# if index is not a valid index, the function should return the original list

def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    new_lst = lst[0:index]
    new_lst.append(lst[index]*2)
    new_lst = new_lst + lst[index+1:]
    return new_lst

print(double_index([3, 8, -10, 12], 2))

###############################################
spaces(23)
###################################################
# function should return a list where all elements in "lst" with an
# index between start and end have been removed
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


###########################################################
spaces(24)
##################################################################
# the function should return "True" if "item" appears in the list more than "n" times
# return "False" otherwise
def more_than_n(lst,item,n):
  x = lst.count(item) 
  if x > n :
    return True
  else :
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

################################################################
spaces(25)
######################################################################
# return either item1 or item2 depending on which item appears more often in lst
#if the two appear the same number of times, return item1

def more_frequent_item(lst,item1,item2):
  x= lst.count(item1)
  y= lst.count(item2)
  if x >= y :
    return item1
  else :
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


######################################################################
spaces(26)
#####################################################################
# if there are an odd number of elementws in "lst", the function should return the middle element
#if there are an even number of elements, the function should return the average of the middle two elements.
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))

#################################################################
spaces(27)
########################################################
# the function add the last two elements of lst together and append the result to "lst"
# it shuold this porcess three times and then return "lst"

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

print(append_sum([1, 1, 2]))

###########################################################
spaces(28)
###################################################################
# function return the last element of the list that contains more elements
# if both lists are the same size, then return the last element of "lst1"
def larger_list(lst1,lst2):
  x= len(lst1)
  y= len(lst2)
  if x >= y : 
    return lst1[x-1]
  else: 
    return lst2[y-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#############################################################3
spaces(29)
##############################################################
# function combine the two lists into the one new list and sort 
#the result. Return the new sorted list
def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sortedList = sorted(unsorted)
  return sortedList

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

###############################################################
spaces(30)
################################################################
# function should append the size of "lst" to the end of lst. The function shuold then return this new list
def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([23, 42, 108]))

#############################################################
spaces(31)
##################################################################
# function shuold return a list of every third number between start and 100(inclusive).
#if start is greater than 100, then it should return an empty list

def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))


######################################
