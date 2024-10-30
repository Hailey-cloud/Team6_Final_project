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
    global transactions
    if transactions.empty:
        print("There are not transactions available.")
        return
    print(transactions)
    while True:  # validate the transaction row
        try:
            row = int(input("Enter the number of the transaction you want to edit: "))
            if 0 <= row <= (len(transactions) - 1):
                break
            else:
                print("Enter a valid number of transaction.")
        except ValueError:
            print("Enter a valid number of transaction.")

    print("Current transaction details: ")
    print(transactions.loc[row, :])  # print the transaction details
    print()
    date, category, description, amount, _ = transactions.loc[row, :]

    # Input new Date
    while True:
        try:
            date_n = input("Enter new date(YYYY - MM - DD) or press Enter to keep current: ")
            if date_n.strip() == "":  # if no date, set old date
                date_n = date
            else:
                date_n = pd.to_datetime(date_n, format="%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    # Input new Category
    while True:
        category_n = input("Enter new category or press Enter to keep current: ")
        if category_n.strip():
            break
        else:
            category_n = category  # if no category, set old category
            break

    # Input new Describe
    while True:
        description_n = input("Enter new description or press Enter to keep current: ")
        if description_n.strip():
            break
        else:
            description_n = description  # if no description, set old description
            break

    # Input new Amount
    while True:
        try:
            amount_n = input("Enter new amount or press Enter to keep current: ")
            if amount_n.strip() == "":
                amount_n = amount  # if no amount, set old amount
                break
            amount_n = float(amount_n)
            if amount_n > 0:
                break
            else:
                print("Amount must be a positive number.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    # Editing the transaction by accessing the row
    transactions.loc[row, ["Date", "Category", "Description", "Amount"]] = [date_n, category_n, description_n, amount_n]
    print(transactions.loc[row, :])
    print("Transaction edited successfully!")

def delete_transaction():
    print("delete_transaction")
def analyze_spending_by_category():
    print("--- Total Spending by Category ---")
    global transactions

    if transactions.empty:
        print("No transactions to display.Import a CSV file at first.")

    else:
        spending_data = transactions[transactions["Type"] == "Expense"]

        total_spending_each_category = spending_data.groupby("Category")["Amount"].sum()
        total_spending_each_category = total_spending_each_category.sort_values(ascending=True)
        print(total_spending_each_category)

        total_spending_each_category.plot(kind="bar",color="orange",grid="True")

        plt.title("total_spending_each_category")
        plt.xlabel("Category")
        plt.ylabel("Total amount (CAD)")

        for index, value in enumerate(total_spending_each_category):
            plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')

        plt.show()
def calculate_average_monthly_spending():
    print("--- Average Monthly Spending ---")
    global transactions

    if transactions.empty:
        print("No transactions to display.Import a CSV File.")

    else:
        spending_data_only_expenses = transactions[transactions["Type"] == "Expense"]

        if spending_data_only_expenses.empty:
            print("No transactions to display.")

        else:
            date_and_expense = spending_data_only_expenses[["Date","Amount"]]
            date_and_expense.loc[:,"Date"] = pd.to_datetime(date_and_expense["Date"])
            date_and_expense.set_index("Date",inplace=True)


            monthly_average = date_and_expense.resample("MS").mean()
            overall_average = monthly_average["Amount"].mean().round(3)
            print(f"Average Monthly Spending is {overall_average}. \n")

            print("--- Details ---\n")
            print(monthly_average)

def show_top_spending_category():
    global transactions
    if transactions.empty:
        print("There are not transactions available.")
    else:
        expenses = transactions[transactions['Type'] == "Expense"]
        top_cat_expenses = expenses.groupby('Category')[['Amount']].sum().sort_values(by='Amount', ascending=False)
        print("The top spending categories are:")
        print(top_cat_expenses)

def visualize_monthly_spending():
    print("visualize_monthly_spending")

def visualize_spending_by_category():
    print("visualize_spending_by_category")

def visualize_spending_distribution():
    print("visualize_spending_distribution")

def save_transactions_to_csv():
    global transactions
    file_path = "sampledata.csv"  # define file path
    if transactions.empty:  # if transactions is empty
        print("There are not transactions yet. No file saved.\n")
        return
    else:
        transactions.to_csv(file_path, index=False, header=True, sep=",")  # write in the file
        print(f"Tasks saved to '{file_path}'.")
        print("The transactions were saved successfully!")

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
