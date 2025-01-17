
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
#* data structure for the expense tracking
expenses = {
  "total_spent": 0,
  "category_spent": {

  },
  "expenses_list":[
    
  ] 
}






def add_new_expense(amount, category, description):
  print(amount, category, description)
  # print(amount)
  expenses["total_spent"] += amount
  expenses["category_spent"]
  expenses["expenses_list"].push({
    
  })


add_new_expense(1.2,"food", ["fruit", "veg"])
print(expenses)
add_new_expense(1.75,"Food", ["tofu"])
print(expenses)
add_new_expense(11.11,"transport", "fuel")
print(expenses)


print(round(expenses["total_spent"], 2))
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