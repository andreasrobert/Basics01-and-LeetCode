print(type(5))
print(type("hello"))
my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list))









# From Python: function arguments (Don't use mutable default arguments)
def update_order(new_item, current_order=[]):
  current_order.append(new_item)
  return current_order
# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)
# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})
# What's in that second order again?
print(order2)

# USING NONE AS A SENTINEL
def add_author(authors_books, current_books=None):
  if current_books is None:
    current_books = []

  current_books.extend(authors_books)
  return current_books



# USING NONE AS A SENTINEL
def update_order(new_item, current_order=None):
  if current_order is None:
    current_order = []    
  current_order.append(new_item)
  return current_order
# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)
# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})
# What's in that second order again?
print(order2)




# UNPACKING MULTIPLE RETURNS
def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper
the_scream, the_whisper = scream_and_whisper("Hello There!")
print(the_scream)
print(the_whisper)

# UNPACKING MULTIPLE RETURNS
def multiple_returns(cool_num1, cool_num2):
  sum_nums = cool_num1 + cool_num2
  div_nums = cool_num1 / cool_num2
  return sum_nums, div_nums
sum_and_div = multiple_returns(20, 10)
print(sum_and_div)
print(sum_and_div[0])


#POSITIONAL ARGUMENT UNPACKING
def shout_strings(*args):
  for argument in args:
    print(argument.upper())
shout_strings("hi", "what do we have here", "cool, thanks!")


# POSITIONAL ARGUMENT UNPACKING
def truncate_sentences(length, *sentences):
  for sentence in sentences:
    print(sentence[:length])
truncate_sentences(8, "What's going on here", "Looks like we've been cut off")