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
