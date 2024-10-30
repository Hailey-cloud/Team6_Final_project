# user_interface.py
from modules.file_operations import import_csv, save_transactions_to_csv
from modules.data_management import add_transaction, edit_transaction, delete_transaction, view_transactions, \
    view_transactions_by_date
from modules.data_analysis import analyze_spending_by_category, calculate_average_monthly_spending, \
    show_top_spending_category
from modules.data_visualization import visualize_monthly_spending, set_category_budget,check_budget_status,income_manage_and_display_the_balance
from modules.data_storage import get_transactions,update_transactions

def main_menu():
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
        # -----Extra------
        print("10. Set Category Budget")
        print("11. Check Budget Status")
        print("12. Income Manage & Display the Balance")
        # -----Extra------

        print("13. Export the CSV")
        print("14. Exit")

        choice = input("Choose an option (0-13): ")

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
        # -----Extra------
        elif choice == "10":
            set_category_budget()
        elif choice == "11":
            check_budget_status()
        elif choice == "12":
            income_manage_and_display_the_balance()
        # -----Extra------

        elif choice == "13":
            save_transactions_to_csv()
        elif choice == "14":
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option.")
