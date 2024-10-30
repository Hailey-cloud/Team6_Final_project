# modules/data_management.py
import pandas as pd
from .data_storage import get_transactions, update_transactions


def view_transactions():
    transactions = get_transactions()
    if transactions.empty:
        print("No transactions to display.")
    else:
        print(transactions)


# ERROR
def view_transactions_by_date():
    transactions = get_transactions()
    print("view_transactions_by_date")
    min_date = transactions["Date"].min()
    max_date = transactions["Date"].max()

    while True:
        try:
            start_view_date = pd.to_datetime(input("Enter the start date(YYYY-MM-DD): "), format="%Y-%m-%d")
            if start_view_date < min_date or start_view_date > max_date:
                print("Invalid date format. Please enter the valid date range.")
                continue
            else:
                break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    while True:
        try:
            end_view_date = pd.to_datetime(input("Enter the end date(YYYY-MM-DD): "), format="%Y-%m-%d")
            if end_view_date < min_date or end_view_date > max_date:
                print("Invalid date format. Please enter the valid date range.")
                continue
            else:
                break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    filtered_data = (transactions["Date"] >= start_view_date) & (transactions["Date"] <= end_view_date)
    filtered_specified_data = transactions[filtered_data]
    print(filtered_specified_data)


def add_transaction():
    transactions = get_transactions()

    while True:
        try:
            date = input("Enter the date (YYYY-MM-DD): ")
            date = pd.to_datetime(date, format="%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    while True:
        category = input("Enter category: ")
        if category.strip():
            break
        else:
            print("Category cannot be empty.")

    while True:
        description = input("Enter description: ")
        if description.strip():
            break
        else:
            print("Description cannot be empty.")

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount > 0:
                break
            else:
                print("Amount must be a positive number.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    while True:
        trans_type = input("Enter type (Expense or Income): ").strip().capitalize()
        if trans_type in ["Expense", "Income"]:
            break
        else:
            print("Invalid type. Please enter either 'Expense' or 'Income'.")

    new_transaction = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Description": [description],
        "Amount": [amount],
        "Type": [trans_type]
    })
    transactions = pd.concat([transactions, new_transaction], ignore_index=True)
    update_transactions(transactions)
    print("Transaction added successfully!")


def edit_transaction():
    transactions = get_transactions()
    if transactions.empty:
        print("There are no transactions available.")
        return
    print(transactions)

    while True:
        try:
            row = int(input("Enter the number of the transaction you want to edit: "))
            if 0 <= row <= (len(transactions) - 1):
                break
            else:
                print("Enter a valid number of transaction.")
        except ValueError:
            print("Enter a valid number of transaction.")

    print("Current transaction details:")
    print(transactions.loc[row, :])
    print()
    date, category, description, amount, _ = transactions.loc[row, :]

    while True:
        try:
            date_n = input("Enter new date(YYYY-MM-DD) or press Enter to keep current: ")
            if date_n.strip() == "":
                date_n = date
            else:
                date_n = pd.to_datetime(date_n, format="%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    while True:
        category_n = input("Enter new category or press Enter to keep current: ")
        if category_n.strip():
            break
        else:
            category_n = category
            break

    while True:
        description_n = input("Enter new description or press Enter to keep current: ")
        if description_n.strip():
            break
        else:
            description_n = description
            break

    while True:
        try:
            amount_n = input("Enter new amount or press Enter to keep current: ")
            if amount_n.strip() == "":
                amount_n = amount
                break
            amount_n = float(amount_n)
            if amount_n > 0:
                break
            else:
                print("Amount must be a positive number.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    transactions.loc[row, ["Date", "Category", "Description", "Amount"]] = [date_n, category_n, description_n, amount_n]
    update_transactions(transactions)
    print("Transaction edited successfully!")


def delete_transaction():
    print("delete_transaction")
