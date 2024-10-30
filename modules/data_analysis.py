# modules/data_analysis.py
from .data_storage import get_transactions

def analyze_spending_by_category():
    transactions = get_transactions()
    if transactions.empty:
        print("No transactions to display. Import a CSV file first.")
    else:
        spending_data = transactions[transactions["Type"] == "Expense"]
        total_spending_each_category = spending_data.groupby("Category")["Amount"].sum().sort_values(ascending=True)
        print(total_spending_each_category)

def calculate_average_monthly_spending():
    print("calculate_average_monthly_spending")

def show_top_spending_category():
    transactions = get_transactions()
    if transactions.empty:
        print("There are no transactions available.")
    else:
        expenses = transactions[transactions['Type'] == "Expense"]
        top_cat_expenses = expenses.groupby('Category')[['Amount']].sum().sort_values(by='Amount', ascending=False)
        print("The top spending categories are:")
        print(top_cat_expenses)
