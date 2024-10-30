# modules/file_operations.py
import pandas as pd
from data_storage import get_transactions, update_transactions

def import_csv():
    global transactions
    file_path = "sampledata.csv"
    try:
        transactions = pd.read_csv(file_path, parse_dates=["Date"])
        update_transactions(transactions)
        print("File imported successfully.")
    except Exception as e:
        print(f"Error importing file: {e}")

def save_transactions_to_csv():
    transactions = get_transactions()
    file_path = "sampledata.csv"
    if transactions.empty:
        print("There are no transactions yet. No file saved.")
    else:
        transactions.to_csv(file_path, index=False, header=True, sep=",")
        print(f"Transactions saved to '{file_path}'.")
