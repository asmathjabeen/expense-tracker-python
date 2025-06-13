
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
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found.")

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
                summary[row[1]] += float(row[2])
        print("\n--- Expense Summary by Category ---")
        for category, total in summary.items():
            print(f"{category}: ₹{total}")
    except FileNotFoundError:
        print("No expenses found.")
