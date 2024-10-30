# modules/data_visualization.py
import matplotlib.pyplot as plt
from .data_storage import get_transactions

def visualize_monthly_spending():
    print("--- Visualize Monthly Spending ---")
    global transactions
    if transactions.empty:
        print("There are not transactions available.")
    else:
        expenses = transactions[transactions['Type'] == "Expense"]
        if expenses.empty:
            print("There are not spending transactions available.")
        else:
            monthly_expenses = (expenses.groupby([expenses['Date'].dt.to_period('M'), 'Category'])['Amount']
                                .sum().reset_index())
            # plot monthly spending
            pivot_expenses = monthly_expenses.pivot(index='Date', columns='Category', values='Amount').fillna(0)
            pivot_expenses.plot(kind='bar', stacked=True, color=['orange', 'cyan', 'lime', 'yellow'], edgecolor="black")
            plt.xlabel("Months")
            plt.ylabel("Values")
            plt.title("Visualize Monthly Spending")
            plt.xticks(rotation=45)
            plt.legend(title='Category')
            plt.tight_layout()
            plt.show()

def visualize_spending_by_category():
    print("visualize_spending_by_category")

def visualize_spending_distribution():
    print("visualize_spending_distribution")
