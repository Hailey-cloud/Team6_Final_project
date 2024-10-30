# modules/data_storage.py
import pandas as pd

# Data Storage
transactions = pd.DataFrame(columns=["Date", "Category", "Description", "Amount", "Type"])

def get_transactions():
    return transactions

def update_transactions(new_transactions):
    global transactions
    transactions = new_transactions