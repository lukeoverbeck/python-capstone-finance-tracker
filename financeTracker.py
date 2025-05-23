print("Welcome to the Personal Finance Tracker!")
data = {}

def print_menu():
  print("\nWhat would you like to do?:\n" \
    "1. Add Expense\n" \
    "2. View All Expenses\n" \
    "3. View Summary\n" \
    "4. Exit\n"
    "Choose an option: ", end="")

# Adds expense to a dictionary, which keeps track of all expenses
# Key: category; value: (description, amount) tuple
def add_expense(data):
  while True:
    try:
      description = input("Enter expense description: ")
      category = input("Enter category: ")
      amount = float(input("Enter amount: "))

      if category not in data:
        data[category] = []

      data[category].append((description, amount))
      print("Expense added.")
      break

    except ValueError:
      print("Invalid input! Please try a valid number.")

# Uses nested for loops to print out the data. This is necessary because the tuples stored as values
# are elements of a list.
def view_expenses(data):
  for category, items in data.items():
    print(f"Category: {category}")
    for description, amount in items:
      print(f"\t- {description}: ${amount}")

# Uses nested for loops to add the amounts to a variable sum for each category. The total for
# each category is printed out at the end of each iteration of the outer loop
def view_summary(data):
  for category, items in data.items():
    sum = 0
    for description, amount in items:
      sum += amount
    print(f"{category}: ${sum}")

while True:
  try:
    print_menu()
    num = int(input())

    if num == 1:
      print()
      add_expense(data)

    elif num == 2:
      print()
      view_expenses(data)

    elif num == 3:
      print()
      view_summary(data)
        
    elif num == 4:
      print()
      print("Goodbye!")
      break
    
    else:
      print("Invalid input! Please try another number.")

  except ValueError as e:
    print("Invalid input! Please try a valid number.")