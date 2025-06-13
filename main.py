
from utils import add_expense, view_expenses, filter_expenses, summarize_expenses
import sys

def menu():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_expenses()
        elif choice == '4':
            summarize_expenses()
        elif choice == '5':
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
