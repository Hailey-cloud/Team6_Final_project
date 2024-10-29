import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# global valuable
transactions = pd.DataFrame(columns=["Date", "Category", "Description", "Amount","Type"])

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
    global transactions

    print("view_transactions_by_date")

    min_date = transactions["Date"].min()
    max_date = transactions["Date"].max()

    while True:
        try:
            start_view_date = pd.to_datetime(input("Enter the start date(YYYY-MM-DD): "), format="%Y-%m-%d")

            if start_view_date < min_date or start_view_date > max_date:
                print("Invalid date format. Please enter the valid date range.")
                continue

            while True:
                try:
                    end_view_date = pd.to_datetime(input("Enter the end date(YYYY-MM-DD): "), format="%Y-%m-%d")
                    if end_view_date < min_date or end_view_date > max_date:
                        print("Invalid date format. Please enter the valid date range.")
                        continue

                    filtered_data = (transactions["Date"] >= start_view_date) & (transactions["Date"] <= end_view_date)

                    filtered_specified_data = transactions[filtered_data]

                    print(filtered_specified_data)

                except ValueError:
                    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
#start dateの入力が終わった後に、enddateの入力だけが間違っていた場合、enddate入力に戻るようにする
#transactionの範囲外の日付が入力された時に、正しく入力するようにする。




def add_transaction():
    global transactions

    # Input Date
    while True:
        try:
            date = input("Enter the date (YYYY-MM-DD): ")
            date = pd.to_datetime(date, format="%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    # Input Category
    while True:
        category = input("Enter category: ")
        if category.strip():
            break
        else:
            print("Category cannot be empty.")

    # Input Describe
    while True:
        description = input("Enter description: ")
        if description.strip():
            break
        else:
            print("Description cannot be empty.")

    # Input Amount
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount > 0:
                break
            else:
                print("Amount must be a positive number.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    # Input Type(Expense,Income)
    while True:
        trans_type = input("Enter type (Expense or Income): ").strip().capitalize()
        if trans_type in ["Expense", "Income"]:
            break
        else:
            print("Invalid type. Please enter either 'Expense' or 'Income'.")

    # Making new transaction
    new_transaction = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Description": [description],
        "Amount": [amount],
        "Type": [trans_type]
    })
    transactions = pd.concat([transactions, new_transaction], ignore_index=True)
    print("Transaction added successfully!")

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
