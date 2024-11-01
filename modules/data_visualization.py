# modules/data_visualization.py
import matplotlib.pyplot as plt
from .data_storage import get_transactions
import pandas as pd
import numpy as np
from .data_storage import get_transactions, transactions

food = 0
rent = 0
utilities = 0
transport = 0
other = 0

def visualize_monthly_spending():
    print("--- Visualize Monthly Spending ---")
    transactions = get_transactions()
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
    global food, rent, utilities, transport, other
    print("Please set the budget for the following categories.")
    while True:
        try:
            food = float(input("Enter your budget for Food: "))
            if food >= 0:
                break
            else:
                print("Budget must be a positive number.")
        except ValueError:
            print("Invalid budget. Please enter a numeric value.")
    # Rent
    while True:
        try:
            rent = float(input("Enter your budget for Rent: "))
            if rent >= 0:
                break
            else:
                print("Budget must be a positive number.")
        except ValueError:
            print("Invalid budget. Please enter a numeric value.")
    # Utilities
    while True:
        try:
            utilities = float(input("Enter your budget for Utilities: "))
            if utilities >= 0:
                break
            else:
                print("Budget must be a positive number.")
        except ValueError:
            print("Invalid budget. Please enter a numeric value.")
    # Transport
    while True:
        try:
            transport = float(input("Enter your budget for Transport: "))
            if transport >= 0:
                break
            else:
                print("Budget must be a positive number.")
        except ValueError:
            print("Invalid budget. Please enter a numeric value.")
    # Other
    while True:
        try:
            other = float(input("Enter your budget for Other expenses: "))
            if other >= 0:
                break
            else:
                print("Budget must be a positive number.")
        except ValueError:
            print("Invalid budget. Please enter a numeric value.")

    # print budget
    print("\nYour budgets have been set:")
    print(f"- Food: ${round(food, 2)}")
    print(f"- Rent: ${round(rent, 2)}")
    print(f"- Utilities: ${round(utilities, 2)}")
    print(f"- Transport: ${round(transport, 2)}")
    print(f"- Other: ${round(other, 2)}")

    # return budget categories
    return food, rent, utilities, transport, other

def check_budget_status():
    global food, rent, utilities, transport, other
    # if not budget
    if food == 0 and rent == 0 and utilities == 0 and transport == 0 and other == 0:
        print("Set budget first before checking (option 10).")
        return

    # dictionary from budget
    budget_dict = {
        "Food": food,
        "Rent": rent,
        "Utilities": utilities,
        "Transport": transport,
        "Other": other
    }

    # get transactions
    transactions = get_transactions()
    if transactions.empty:
        print("Not transactions available for comparison.")
        return

    # from transactions, get expenses
    expense = transactions[transactions['Type'] == "Expense"]
    if expense.empty:
        print("There are not spending transactions available.")
        return

    # from expenses get by categories
    cat_exp = expense.groupby('Category')['Amount'].sum()
    food_exp = cat_exp.get("Food", 0)   # cat_exp.get("label", default_value)  to get the value of the label
    rent_exp = cat_exp.get("Rent", 0)
    utilities_exp = cat_exp.get("Utilities", 0)
    transport_exp = cat_exp.get("Transport", 0)
    # other_exp = cat_exp.get("Other", 0)
    other_exp = cat_exp[cat_exp.index.isin(["Food", "Rent", "Utilities", "Transport"]) == False].sum()

    # dictionary from expenses
    expense_dict = {
        "Food": food_exp,
        "Rent": rent_exp,
        "Utilities": utilities_exp,
        "Transport": transport_exp,
        "Other": other_exp
    }
    print("--- Budget Status ---")
    print("- Category: Expenses / Budget")
    for k_exp,e in expense_dict.items():
        for k_bud,b in budget_dict.items():
            if k_exp == k_bud:
                # if alert
                alert = ""
                if e > b:
                    alert = "(Alert: Exceeded budget!)"
                elif b != 0:
                    if 1 > (e / b) >= 0.9:
                        alert = "(Warning: Close to budget!)"
                print(f"- {k_bud}: ${e} / ${b}  {alert}")

    print("\nSuggestions:")
    ok = 0
    for k_exp,e in expense_dict.items():
        for k_bud,b in budget_dict.items():
            if k_exp == k_bud:
                if b != 0:
                    if 1 > (e / b) >= 0.9:
                        print(f"- Monitor {k_bud} spending closely to avoid exceeding the budget.")
                        ok +=1
                if e >= b and not (e == 0 and b == 0):
                    print(f"- Consider reducing {k_bud} spending or adjusting the budget.")
                    ok += 1

    if ok == 0:
        print("- You are within budget. Keep up the good work!")
    elif 0 < ok < 5:
        print("- You are on track for other categories.")

    # plot the budget vs expenses
    x = np.array([0, 1, 2, 3, 4])
    width = 0.25  # Width of each bar
    plt.bar(x - width / 2, expense_dict.values(), width, color='blue', edgecolor='black', label="Expenses")
    plt.bar(x + width / 2, budget_dict.values(), width, color='salmon', edgecolor='black', label="Budget")
    plt.title("Expenses vs Budget per categories")
    plt.xlabel("Categories")
    plt.ylabel("Amount")
    plt.xticks(x,['Food', 'Rent', 'Utilities', 'Transport', 'Other'])
    plt.legend()
    plt.show()

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









