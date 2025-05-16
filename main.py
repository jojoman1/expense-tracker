import csv
from datetime import datetime

FILE_NAME = 'expenses.csv'

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    amount = input("Enter amount: ₹ ")
    category = input("Enter category (food, travel, etc.): ")
    note = input("Enter note: ")
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])
    print("✅ Expense added!")

def view_expenses():
    print("\n📊 All Expenses:")
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

def main():
    print("💰 Personal Expense Tracker")
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()