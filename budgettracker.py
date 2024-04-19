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

