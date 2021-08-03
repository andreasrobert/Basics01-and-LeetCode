def spaces(p):
    print("\n----------------------------------------------------- \n#"+str(p))
print("-------------------- IT STARTS HERE -----------------------")


# choose which letter 
my_name = "jeff"
first_initial = my_name[0]

# other example with a more specific choosing of which index
# [ THIS : ..   ] which index it starts
# [  ..  : THIS ] which index it stops (element of (index) wont be in it )
last_name = "Villanueva"
new_account = last_name[:5]
temp_password = last_name[2:6]

#other example
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)

#1
spaces(1)
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)

#another same exaple

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name,last_name):
  x = len(first_name)
  y = len(last_name)
  
  first = first_name[x-3:]
  last = last_name[y-3:]
  
  return first+last

print(password_generator(first_name,last_name))

# using negative indices
company_motto = "i'm lovin it"

second_to_last_word = company_motto[-2]
final_word = company_motto [-2: ]

#other example
first_name = "Bob"
last_name = "Daily"
# first_name[0] = "R" cant use this, cant change an individual character

fixed_first_name = "R" + first_name[1:]

spaces(2)
#instead of using len(), we can use loops.. for reasons
def get_length(word):
  length = 0
  
  for x in word:
    length += 1
    
  return length

#another simple example 
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

#and another one
def contains(big_string, little_string):
  return little_string in big_string

# return a list with all of the letters they have in common

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print(common_letters("banana","walnut"))


# REVIEW
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password


# 
def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])

print_some_characters("watermelon")