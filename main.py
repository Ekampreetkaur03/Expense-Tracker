
import json
import os
from datetime import date

FILE_NAME = "expenses.json"

CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Education",
    "Bills",
    "Health",
    "Other"
]

# Load expenses from JSON
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        print("Warning: Invalid data format. Starting with an empty list.")
        return []

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read expenses.json.")
        return []


# Save expenses to JSON
def save_expenses():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
    except OSError:
        print("Error: Could not save expenses.")


expenses = load_expenses()


# Display available categories
def show_categories():
    print("\nAvailable Categories:")

    for number, category in enumerate(CATEGORIES, start=1):
        print(f"{number}. {category}")


# Add a new expense
def add_expense():
    print("Add Expense")

    description = input("Enter expense description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    while True:
        try:
            amount = float(input("Enter amount (₹): "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    show_categories()

    while True:
        try:
            choice = int(input("Select category number: "))

            if 1 <= choice <= len(CATEGORIES):
                category = CATEGORIES[choice - 1]
                break

            print("Please select a valid category number.")

        except ValueError:
            print("Enter a number from the category list.")

    expense = {
        "description": description,
        "amount": round(amount, 2),
        "category": category,
        "date": date.today().isoformat()
    }

    expenses.append(expense)
    save_expenses()

    print("\nExpense added successfully!")
    print(f"Description: {description}")
    print(f"Amount: ₹{amount:.2f}")
    print(f"Category: {category}")


# Display all expenses
def view_expenses():
    print("All Expenses")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"\nExpense {number}")
        print("Description:", expense["description"])
        print(f"Amount: ₹{expense['amount']:.2f}")
        print("Category:", expense["category"])
        print("Date:", expense["date"])

    print(f"\nTotal expenses: ₹{calculate_total():.2f}")


# Search expenses by category
def search_expenses():
    print("\n--- Search Expenses ---")

    show_categories()

    while True:
        try:
            choice = int(input("Select category number to search: "))

            if 1 <= choice <= len(CATEGORIES):
                category = CATEGORIES[choice - 1]
                break

            print("Please select a valid category.")

        except ValueError:
            print("Please enter a number.")

    found = [
        expense for expense in expenses
        if expense["category"] == category
    ]

    if not found:
        print(f"No expenses found in {category}.")
        return

    print(f"\nExpenses in {category}:")

    for expense in found:
        print(
            f"{expense['date']} | "
            f"{expense['description']} | "
            f"₹{expense['amount']:.2f}"
        )

    category_total = sum(item["amount"] for item in found)
    print(f"Category total: ₹{category_total:.2f}")


# Calculate total spending
def calculate_total():
    return sum(expense["amount"] for expense in expenses)


# Calculate spending by category
def category_summary():
    print("Category-wise Spending")

    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in totals:
            totals[category] = 0

        totals[category] += amount

    for category, amount in totals.items():
        print(f"{category}: ₹{amount:.2f}")


# Display complete spending summary
def spending_summary():
    print("Spending Summary")

    if not expenses:
        print("No expenses recorded yet.")
        return

    total = calculate_total()

    print("Number of expenses:", len(expenses))
    print(f"Total spending: ₹{total:.2f}")

    category_summary()

    highest = max(expenses, key=lambda item: item["amount"])

    print("\nHighest single expense:")
    print("Description:", highest["description"])
    print(f"Amount: ₹{highest['amount']:.2f}")
    print("Category:", highest["category"])


# Main menu
def main():
    while True:
        print("EXPENSE TRACKER")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses by Category")
        print("4. Calculate Total Expenses")
        print("5. Category-wise Spending")
        print("6. Spending Summary")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expenses()

        elif choice == "4":
            print(f"\nTotal spending: ₹{calculate_total():.2f}")

        elif choice == "5":
            category_summary()

        elif choice == "6":
            spending_summary()

        elif choice == "7":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
