import os
import json
from collections import defaultdict

# Function that loads transactions from file
def load_transactions():
  try:
    if os.path.exists("transactions.json"):
      with open("transactions.json", "r") as file:
        return json.load(file)
  except:
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
  return sum(item["amount"] for item in transactions["income"])
    
#Function that calculates remaining monthly income after expenses
def calculate_remaining_income(transactions):
  return calculate_income(transactions) - calculate_expenses(transactions)

#Function that summarizes expenses by category
def summarize_expenses(transactions):
    expense_categories = defaultdict(float)
    print("\nExpense Summary:")
    for index, expense in enumerate(transactions["expenses"]):
        expense_categories[expense["category"]] += expense["amount"]
        print(f"{index + 1}. {expense['category']}: {expense['amount']}")
    
#Function to remove an expense   
def remove_expense(transactions):
  while True:
    summarize_expenses(transactions)
    print("Please enter the expense that you would like to remove: ")
    try:
      expense_to_remove = int(input("> "))
      del transactions["expenses"][expense_to_remove - 1]
    except:
      print("Invalid input. Please try again.")

#Main function 
def main():
  transactions = load_transactions()
  while True:
    print("\nStudent Monthly Budget Tracker Menu:")
    print("1. Log Income")
    print("2. Log Expense")
    print("3. Remove an Expense")
    print("4. Analyze Budget")
    print("5. Summary of Expenses")
    print("6. Exit")
    choice = input("Please enter a menu choice [1-5]: ")
    if choice == "1":
      log_income(transactions)
    elif choice == "2":
      log_expense(transactions)
    elif choice == "3":
      remove_expense(transactions)
    elif choice == "4":
      print("\nBudget Analysis:")
      print(f"Total Income: {calculate_income(transactions)}")
      print(f"Total Expenses: {calculate_expenses(transactions)}")
      print(f"Remaining Income: {calculate_remaining_income(transactions)}")
    elif choice == "5":
      summarize_expenses(transactions)
    elif choice == "6":
      print("Exiting the program...")
      with open("transactions.json", "w") as file:
        return {"expenses": [], "income": []}
    else:
      print("You entered an invalid choice. Please retry and enter a number between 1 and 5.")
  
#Runs main function only when running this file directly
if __name__ == "__main__":
  main()
