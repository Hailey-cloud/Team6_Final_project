# modules/data_analysis.py
import matplotlib.pyplot as plt
import pandas as pd
from .data_storage import get_transactions

def analyze_spending_by_category():
    print("--- Total Spending by Category ---")
    transactions = get_transactions()
    if transactions.empty:
        print("No transactions to display. Import a CSV file first.")
    else:
        spending_data = transactions[transactions["Type"] == "Expense"]

        total_spending_each_category = spending_data.groupby("Category")["Amount"].sum()
        total_spending_each_category = total_spending_each_category.sort_values(ascending=True)
        print(total_spending_each_category)

        total_spending_each_category.plot(kind="bar", color="orange", grid="True")

        plt.title("total_spending_each_category")
        plt.xlabel("Category")
        plt.ylabel("Total amount (CAD)")

        for index, value in enumerate(total_spending_each_category):
            plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')

        plt.show()

def calculate_average_monthly_spending():
    print("--- Average Monthly Spending ---")
    transactions = get_transactions()
    if transactions.empty:
        print("No transactions to display.Import a CSV File.")

    else:
        spending_data_only_expenses = transactions[transactions["Type"] == "Expense"]

        if spending_data_only_expenses.empty:
            print("No transactions to display.")

        else:
            monthly_average = spending_data_only_expenses.groupby(spending_data_only_expenses['Date']
                                                                  .dt.to_period('M'))['Amount'].mean().round(2)
            overall_average = monthly_average.mean().round(2)
            print(f"Average Monthly Spending is ${overall_average}. \n")
            print("--- Details ---")
            print(monthly_average)


def show_top_spending_category():
    transactions = get_transactions()
    if transactions.empty:
        print("There are no transactions available.")
    else:
        expenses = transactions[transactions['Type'] == "Expense"]
        if expenses.empty:
            print("There are not spending transactions available.")
        else:
            top_cat_expenses = expenses.groupby('Category')[['Amount']].sum()
            top_amount = top_cat_expenses['Amount'].max()
            top_cat = top_cat_expenses['Amount'].idxmax()
            print("--- Top spending category ---")
            print(f"{top_cat} with ${top_amount} total spending.")
