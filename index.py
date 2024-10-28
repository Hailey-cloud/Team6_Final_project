import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# global valuable
transactions = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])

def import_csv():
    global transactions
    # file_path = input("Enter file path: ")
    file_path = "sampledata.csv"
    try:
        transactions = pd.read_csv(file_path, parse_dates=["Date"])
        print("File imported successfully.")
    except Exception as e:
        print(f"Error importing file: {e}")


def view_transactions():
    if transactions.empty:
        print("No transactions to display.")
    else:
        print(transactions)

def view_transactions_by_date():
    print("view_transactions_by_date")

def add_transaction():
    print("add_transaction")

def edit_transaction():
    print("edit_transaction")

def delete_transaction():
    print("delete_transaction")

def analyze_spending_by_category():
    print("analyze_spending_by_category")

def calculate_average_monthly_spending():
    print("calculate_average_monthly_spending")

def show_top_spending_category():
    print("show_top_spending_category")

def visualize_monthly_spending():
    print("visualize_monthly_spending")

def visualize_spending_by_category():
    print("visualize_spending_by_category")

def visualize_spending_distribution():
    print("visualize_spending_distribution")

def save_transactions_to_csv():
    print("save_transactions_to_csv")

def process_choice(choice):
    if choice == "0":
        import_csv()
    elif choice == "1":
        view_transactions()
    elif choice == "2":
        view_transactions_by_date()
    elif choice == "3":
        add_transaction()
    elif choice == "4":
        edit_transaction()
    elif choice == "5":
        delete_transaction()
    elif choice == "6":
        analyze_spending_by_category()
    elif choice == "7":
        calculate_average_monthly_spending()
    elif choice == "8":
        show_top_spending_category()
    elif choice == "9":
        visualize_monthly_spending()
    elif choice == "10":
        save_transactions_to_csv()
    elif choice == "11":
        print("Exiting the Personal Finance Tracker. Goodbye!")
        return False
    # Extended Features
    elif choice == "12":
        print("When we finish the standard task, we do the extended task.")
    elif choice == "13":
        print("When we finish the standard task, we do the extended task.")
    elif choice == "14":
        print("When we finish the standard task, we do the extended task.")
    else:
        print("Invalid choice, please select a valid option.")
    return True

def run():
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("0. Import a CSV File")
        print("1. View All Transactions")
        print("2. View Transactions by Date Range")
        print("3. Add a Transaction")
        print("4. Edit a Transaction")
        print("5. Delete a Transaction")
        print("6. Analyze Spending by Category")
        print("7. Calculate Average Monthly Spending")
        print("8. Show Top Spending Category")
        print("9. Visualize Monthly Spending Trend")
        print("10. Save Transactions to CSV")
        print("11. Exit")
        print("12. Extended Features - Income Management")
        print("13. Extended Features - Budget Setting and Alerts")
        print("14. Extended Features - Suggestions for Better Budgeting")

        choice = input("Choose an option (0-14): ")
        if not process_choice(choice):
            break

# Run application
if __name__ == "__main__":
    run()
