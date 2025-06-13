

import csv
from datetime import datetime
from collections import defaultdict

CSV_FILE = 'expenses.csv'

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    note = input("Enter a note (optional): ")

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("Expense added successfully.")

def view_expenses():
    print("\n--- All Expenses ---")
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            for idx, row in enumerate(expenses, start=1):
                if len(row) >= 3:
                    date = row[0]
                    category = row[1]
                    amount = row[2]
                    note = row[3] if len(row) > 3 else "—"
                    print(f"{idx}. Date: {date} | Category: {category} | Amount: ₹{amount} | Note: {note}")
                else:
                    print(f"{idx}. Incomplete data: {row}")
    except FileNotFoundError:
        print("expenses.csv not found. Add an expense first.")
    except Exception as e:
        print(f"Error while reading expenses: {e}")



def filter_expenses():
    filter_by = input("Filter by 'date' or 'category': ").strip().lower()
    keyword = input("Enter value to filter by: ").strip()

    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if filter_by == 'date' and row[0] == keyword:
                    print(row)
                elif filter_by == 'category' and row[1].lower() == keyword.lower():
                    print(row)
    except FileNotFoundError:
        print("No expenses found.")

def summarize_expenses():
    summary = defaultdict(float)
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1].strip().lower()
                amount = float(row[2])
                summary[category] += amount
        print("\n--- Expense Summary by Category ---")
        for category, total in summary.items():
            print(f"{category.capitalize()}: ₹{total}")
    except FileNotFoundError:
        print("No expenses found.")
