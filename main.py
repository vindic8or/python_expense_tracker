
# ? Boiler plate. Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")
#------------------------------------------------------

#?----------------- User name input, and greeting.
user = "Guest"
# input("Please enter username: ")
print(f"Hello, {user}. \nExpenses aren't fun. \nLet me help you.")

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


user_entry()

# ! a few test cases
# add_new_expense(1.2,"food", "fruit, veg")
# add_new_expense(1.75,"Food", "tofu, seitan")

# add_new_expense(11.11,"transport", "fuel")
# print(expenses)

# !

# *prints total amount spent, rounded to two decimals after the separator
def show_total_spent():
  print(f'Total spent: {round(expenses["total_spent"], 2)}')





# print(expenses["category_spent_on"])
# expenses["total_spent"] += 1.1

# print(expenses["total_spent"]) 
  # print(f'Total spent on {category.lower()}: {expenses["category_spent_on"]}')
  # expenses["category_spent_on"] = {category.lower() : amount =+ amount}






#?-----------------






# first_expense = {
#   "amount": 21.93,
#   "category" : "food",
#   "description": ["fruit", "veg", "snacks"]
# }

# expenses.update()

print(expenses)

show_total_spent()




















#------------------------------------------------------
# ? Boiler plate. Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")