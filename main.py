
# ? Boiler plate. Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")
#------------------------------------------------------

#?-----------------1 User name input, and greeting.
user = "Guest"
# input("Please enter username: ")
print(f"Hello, {user}. \nExpenses aren't fun. \nLet me help you.")

#TODO under construction
#?-----------------2 Expense logging

#* data structure and initialisation of the expense tracking
expenses = {
  "total_spent": 0,
  "category_spent_on": {

  },
  "expenses_list":[
    
  ] 
}






def add_new_expense(amount, category, description):
  # print(amount, category, description)
  # print(amount)
# *increases the counter of total_spent
  expenses["total_spent"] += amount

# *if category exists, it updates it's value_spent_on
  if category.lower() in expenses["category_spent_on"]:
    expenses["category_spent_on"].update({category.lower(): expenses["category_spent_on"][category.lower()] + amount})

# *creates a category with initial value
  else: 
    expenses["category_spent_on"].update({category.lower(): amount})
  # expenses["category_spent_on"] = {category.lower() : amount =+ amount}
  print(f'Total spent on {category}: {expenses["category_spent_on"]}')
  # expenses["expenses_list"].push({

  # })


add_new_expense(1.2,"food", ["fruit", "veg"])
# print(expenses)
add_new_expense(1.75,"Food".lower(), ["tofu"])
# print(expenses)
add_new_expense(11.11,"transport", "fuel")
print(expenses)


print(round(expenses["total_spent"], 2))
print(expenses["category_spent_on"])
# expenses["total_spent"] += 1.1

# print(expenses["total_spent"]) 

#TODO -------------









#?-----------------






first_expense = {
  "amount": 21.93,
  "category" : "food",
  "description": ["fruit", "veg", "snacks"]
}

# expenses.update()

# print(expenses)






















#------------------------------------------------------
# ? Boiler plate. Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")