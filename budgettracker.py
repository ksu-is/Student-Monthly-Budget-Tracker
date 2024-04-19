import os
import json
from collections import defaultdict

# Function that loads transactions from file
def load_transactions():
  if os.path.exists("transactions.json"):
    with open("transactions.json", "r") as file:
      return json.load(file)
  else:
    return {"expenses": [], "income": []}

# Function that saves transactions to file
def save_transactions(transactions):
  with open("transactions.json", "w") as file:
    json.dump(transactions, file, indent=4)

#Function that logs an expense
def log_expense(transactions):
  category = input("Please enter an expense category: ")
  amount = float(input("Now enter the expense amount: "))
  transactions["expenses"].append({"category": category, "amount": amount})
  save_transactions(transactions)
  print("Thank you. Your expense was logged successfully.")

#Function that logs your income
def log_income(transactions):
  category = input("Please enter an income category: ")
  amount = float(input("Now enter the income amount: "))
  transactions["income"].append({"category": category, "amount": amount})
  save_transactions(transactions)
  print("Thank you. Your income was logged successfully.")

#Function that calculates total expenses
def calculate_expenses(transactions):
  return sum(item["amount"] for item in transactions["expenses"])
    
#Function that calculates income
def calculate_income(transactions):
  return sum(transactions["income"])

#Function that calculates remaining monthly income after expenses
def calculate_remaining_income(transactions):
  return calculate_income(transactions) - calculate_expenses(transactions)

#Function that summarizes expenses by category
def summarize_expenses(transactions):
  expense_categories = defaultdict(float)
  for expense in transactions["expenses"]:
    expense_categories[expense["category"]] += expense["amount"]

  print("\nExpense Summary:")
  for category, amount in expense_categories.items():
    print(f"{category}: {amount}")

#Main function 
def main():
  transactions = load_transactions()
  while True:
    print("\nStudent Monthly Budget Tracker Menu:")
    print("1. Log Expense")
    print("2. Log Income")
    print("3. Analyze Budget")
    print("4. Summary of Expenses")
    print("5. Exit")
    choice = input("Please enter a menu choice [1-5]")
    if choice == "1":
      log_expense(transactions)
    elif choice == "2":
      log_income(transactions)
    elif choice == "3":
      print("\nBudget Analysis:")
      print(f"Total Income: {calculate_income(transactions)}")
      print(f"Total Expenses: {calculate_expenses(transactions)}")
      print(f"Remaining Income: {calculate_remaining_income(transactions)}")
    elif choice == "4":
      summarize_expenses(transactions)
    elif choice == "5":
      print("Exiting the program...")
      break
    else:
      print("You entered an invalid choice. Please retry and enter a number between 1 and 5.")
