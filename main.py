
# ? Boiler plate. Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")
#------------------------------------------------------

#! https://github.com/vindic8or/python_expense_tracker 
#! still needs work, but should have full functionality
#* By Algirdas Varnagiris
#?----------------- User name input, and greeting.
user = input("Please enter username: ")
print(f"Hello, {user}. \nExpenses aren't fun. \nLet me help you.\n--------")

#?----------------- Expense logging

#* data structure and initialisation of the expense tracking table. Stores data.
expenses = {
  "total_spent": 0,
  "category_spent_on": {},
  "expenses_list":[] 
}


# ?-----------------function that handles the data for the table
def add_new_expense(amount, category, description):
# *increases the counter of total_spent
  expenses["total_spent"] += amount

# *if category exists, it updates it's value_spent_on
  if category.lower() in expenses["category_spent_on"]:
    expenses["category_spent_on"].update({category.lower(): expenses["category_spent_on"][category.lower()] + amount})
# *otherwise creates a category with initial value
  else: 
    expenses["category_spent_on"].update({category.lower(): amount})
  
# *adds the items to a list
  expenses["expenses_list"].append({
    "amount" : amount,
    "category": category.lower(),
    "description": description
  })


def user_entry():
  entering_data = True

  while entering_data:
    user_entry = float(input("Please enter the amount spent as a positive digital number: "))
    user_category = input("Please enter expense category: ").lower()
    user_description = input("Please enter the purchase description: ").lower()
    try:
      if user_entry > 0 and len(user_category) > 0 and len(user_description) >0: 
        print(user_entry)
        print(user_category)
        print(user_description)
      else: continue
    except:
      continue
    entering_data = False
    add_new_expense(user_entry, user_category, user_description)




# *prints total amount spent, rounded to two decimals after the separator
def show_total_spent():
  print(f'Total spent: {round(expenses["total_spent"], 2)}')

def amount_spent_in_category(dict):
  for key, value in dict.items():
    print(f'Category: {key}, total spent: {round(value, 2)}.')

def show_expense_list(list):
  for purchase in list:
    print(purchase)

data_entry = True

while data_entry:
  user_entry()
  stop = input("Would you like to add another expense? y/n?")
  if stop == "y":
    continue
  else:
    data_entry = False
    break

# ! a few test cases
# add_new_expense(1.2,"food", "fruit, veg")
# add_new_expense(1.75,"Food", "tofu, seitan")

# add_new_expense(11.11,"transport", "fuel")
# add_new_expense(12.12,"transport", "tickets")

# add_new_expense(0.12,"etc", "gum")
# add_new_expense(85.20,"etc", "random things")

# !-------------------------------

#?----------------- Show the information to the user once data entry has been finished

show_total_spent()
amount_spent_in_category(expenses["category_spent_on"])
show_expense_list(expenses["expenses_list"])

print(f'Thank you for using the expense tracker, {user}!')

















#------------------------------------------------------
# ? Boiler plate. Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")