# modules/data_visualization.py
import matplotlib.pyplot as plt
from .data_storage import get_transactions
import pandas as pd

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

def set_category_budget():
    print("1111111")

def check_budget_status():
    print("22222222")

def income_manage_and_display_the_balance():
        print("---calculate_average_monthly_spending---")

        transactions = get_transactions()

        if transactions.empty:
            print("No transactions to display.Import a CSV file at first.")
            return

        try:

                while True:
                    try:
                            monthly_income_user_input = int(input("Enter your income: "))
                            if monthly_income_user_input < 0:
                                raise ValueError("Income cannot be negative.")
                            break
                    except ValueError as ve:
                        print(f"Error: {ve}. Please try again.")

                monthly_income_details = input("Enter the income detail: ")

                while True:
                    try:
                        monthly_income_date = pd.to_datetime(input("Enter the date that you get your income(YYYY-MM): "),
                                             format="%Y-%m")
                        if pd.isna(monthly_income_date):
                            raise ValueError("Invalid date format. Please enter in YYYY-MM format.")

                        specific_month = monthly_income_date.strftime('%Y-%m')
                        available_months = transactions['Date'].dt.strftime('%Y-%m').unique()
                        if specific_month not in available_months:
                            raise ValueError(
                                f"No data exists for {specific_month}. Available months are: {', '.join(sorted(available_months))}")
                        break
                    except ValueError as e:
                        print(f"Error: {str(e)}")
                        continue

                past_income_of_the_month = transactions[transactions["Type"] == "Income"]["Amount"].sum()
                total_income_of_the_month = past_income_of_the_month + monthly_income_user_input
                print(f"Total Income is ${total_income_of_the_month}")

                specific_month = monthly_income_date.strftime('%Y-%m')
                total_expenses_in_the_month = transactions[(transactions["Type"] == "Expense") & (transactions["Date"].dt.strftime('%Y-%m') == specific_month)]

                past_expenses_of_the_month = total_expenses_in_the_month["Amount"].sum()
                print(f"Total Expenses is ${past_expenses_of_the_month}")

                the_gap_of_income_expenses = total_income_of_the_month - past_expenses_of_the_month
                print(f"The gap between income and expenses is $ {the_gap_of_income_expenses}")

        # condition
                if total_income_of_the_month != 0:
                    ratio_of_expenses = (past_expenses_of_the_month / total_income_of_the_month) * 100

                else:
                    ratio_of_expenses = 0
                    print("You don't use your money yet.")

                if ratio_of_expenses <= 50:
                    print(f"Amazing! Your expense ratio is {ratio_of_expenses.round(2)}%.")
                elif ratio_of_expenses > 50 and ratio_of_expenses <= 70:
                    print(f"Good job! Your expense ratio is {ratio_of_expenses.round(2)}%.")
                elif ratio_of_expenses > 70 and ratio_of_expenses <= 100:
                    print(f"Be careful! Your expense ratio is {ratio_of_expenses.round(2)}%.")
                elif ratio_of_expenses >= 100:
                    print(f"Alert! Your expenses exceed your income.")


            #Plot Visualization
                monthly_data = transactions.copy()
                monthly_data['Month'] = monthly_data['Date'].dt.strftime('%Y-%m')


                monthly_incomes = monthly_data[monthly_data['Type'] == 'Income'].groupby('Month')['Amount'].sum()

                if specific_month in monthly_incomes:
                    monthly_incomes[specific_month] += monthly_income_user_input
                else:
                    monthly_incomes[specific_month] = monthly_income_user_input


                monthly_expenses = monthly_data[monthly_data['Type'] == 'Expense'].groupby('Month')['Amount'].sum()

                plt.figure(figsize=(14, 8))
                plt.plot(monthly_incomes.index, monthly_incomes.values, color="red", label='Total Income', marker='o')
                plt.plot(monthly_expenses.index, monthly_expenses.values, color="green", label='Total Expenses', marker='o')

                plt.title('Monthly Income vs Expenses')
                plt.xlabel('Month')
                plt.ylabel('Amount ($)')
                plt.grid(True)
                plt.legend()

                plt.show()

            #Pie chart

                monthly_expenses_by_category = transactions[(transactions["Type"] == "Expense") & (transactions["Date"].dt.strftime('%Y-%m') == specific_month)].groupby("Category")["Amount"].sum()

                if not monthly_expenses_by_category.empty:

                # subplot1
                    plt.figure(figsize=(10, 8))

                    plt.subplot(1, 2, 1)

                    income_expense_data = [total_income_of_the_month, past_expenses_of_the_month]
                    labels = ['Total Income', 'Total Expenses']
                    colors = ['lightgreen','lightcoral']
                    plt.pie(income_expense_data, colors=colors, autopct='%1.1f%%', startangle=90,shadow =True)
                    plt.title(f'Income vs Expenses Distribution\n({monthly_income_date.strftime("%Y-%m")})')
                    plt.legend(labels,loc="upper right")

                # subplot2


                    plt.subplot(1, 2, 2)
                    categories = monthly_expenses_by_category.index
                    category_values = monthly_expenses_by_category.values
                    plt.pie(monthly_expenses_by_category.values,autopct='%1.1f%%',startangle=90, shadow = True)
                    plt.title(f'Expense Categories Distribution\n({monthly_income_date.strftime("%Y-%m")})')
                    plt.legend(categories,loc="upper right")

                    plt.show()

        except Exception as e:
                print(f"An unexpected error occurred: {e}")









