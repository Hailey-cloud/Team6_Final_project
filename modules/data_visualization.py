# modules/data_visualization.py
import matplotlib.pyplot as plt
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
    print("33333333")