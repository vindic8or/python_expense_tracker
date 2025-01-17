
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

#?-----------------2 Expense logging

def add_new_expense(amount, category, description):
  print("test")




add_new_expense(1,2,3)


# *under construction
# print(2+2)
testvar = print(1+2)


# testdict = {

# }






#?-------




expenses = {
  
}

first_expense = {
  "amount": 21.93,
  "category" : "food",
  "description": ["fruit", "veg", "snacks"]
}

expenses.update()

print(expenses)






















#------------------------------------------------------
# ? Boiler plate. Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")