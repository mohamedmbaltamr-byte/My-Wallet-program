import json
import os
from operator import itemgetter

# --- UTILITY FUNCTIONS (The 'my_class' logic) ---

def get_number_only(prompt="Enter a number: "):
    """Ensures user input is a valid float."""
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a numerical value.")

def choose_option(options_list):
    """Displays a menu and returns the selected index."""
    print("\n--- Choose one of the options ---")
    for i, option in enumerate(options_list):
        print(f"[{i}] - {option}")
    
    while True:
        choice = get_number_only("\nSelect option number: ")
        if 0 <= choice < len(options_list):
            return int(choice)
        print(f"⚠️ Please choose a number between 0 and {len(options_list)-1}")

def get_entry_details(item_prompt, price_prompt, currency="LYD"):
    """Handles the input for a new expense or income entry."""
    item_name = input(item_prompt).strip().title()
    item_price = get_number_only(price_prompt)
    # Formatting entry: (Name, Price, Currency)
    entry_tuple = (f"{item_name}:".ljust(20), item_price, currency)
    return item_name, item_price, entry_tuple

# --- MAIN PROGRAM ---

FILE_NAME = "wallet_data.json"

def main():
    print("\n" + "*"*40)
    print("Welcome to Your Smart Wallet".center(40))
    print("*"*40)

    # Initializing data structures
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            list_expenses = data.get("list_expenses", [])
            list_added = data.get("list_added", [])
            total_prices = data.get("total_prices", 0)
            amount_of_money = data.get("amount_of_money", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\n📝 No previous data found. Creating a new wallet...")
        list_expenses, list_added = [], []
        total_prices, amount_of_money = 0, 0

    # Currency setup
    curr_choice = choose_option(["Libyan Dinar (LYD)", "US Dollar (USD)"])
    currency = "LYD" if curr_choice == 0 else "USD"

    while True:
        menu_items = [
            "Financial Report", "Add Expense", "Add Income", 
            "Save Data", "Reset/Delete Data", "Exit"
        ]
        option = choose_option(menu_items)

        if option == 0:  # FINANCIAL REPORT
            print("\n" + "="*30)
            print("📊 FINANCIAL REPORT")
            
            print("\n🔻 EXPENSES:")
            # Sorting by price (index 1 of the tuple)
            for idx, entry in enumerate(sorted(list_expenses, key=itemgetter(1), reverse=True), 1):
                print(f"  {idx}. {entry[0]} {entry[1]:.2f} {entry[2]}")
            print(f"  {'Total:'.ljust(20)} {total_prices:.2f} {currency}")

            print("\n🔺 INCOME/ADDED:")
            for idx, entry in enumerate(sorted(list_added, key=itemgetter(1), reverse=True), 1):
                print(f"  {idx}. {entry[0]} {entry[1]:.2f} {entry[2]}")
            print(f"  {'Total:'.ljust(20)} {amount_of_money:.2f} {currency}")
            
            savings = amount_of_money - total_prices
            print("\n" + f" CURRENT SAVINGS: {savings:.2f} {currency} ".center(50, "*"))
            input("\nPress ENTER to return to menu...")

        elif option == 1:  # ADD EXPENSE
            while True:
                sub_opt = choose_option(["Add New Expense", "Back to Main Menu"])
                if sub_opt == 0:
                    _, price, entry = get_entry_details("Expense Name: ", "Amount: ", currency)
                    total_prices += price
                    list_expenses.append(entry)
                    print("✅ Expense added.")
                else: break

        elif option == 2:  # ADD INCOME
            while True:
                sub_opt = choose_option(["Add New Income", "Back to Main Menu"])
                if sub_opt == 0:
                    _, price, entry = get_entry_details("Source Name: ", "Amount: ", currency)
                    amount_of_money += price
                    list_added.append(entry)
                    print("✅ Income added.")
                else: break

        elif option == 3:  # SAVE DATA
            data = {
                "list_expenses": list_expenses,
                "list_added": list_added,
                "total_prices": total_prices,
                "amount_of_money": amount_of_money
            }
            with open(FILE_NAME, "w") as f:
                json.dump(data, f, indent=4) # indent=4 makes the JSON file readable
            print("💾 Data saved successfully!")

        elif option == 4:  # DELETE DATA
            confirm = input("⚠️ Are you sure you want to delete all data? (yes/no): ")
            if confirm.lower() == 'yes':
                if os.path.exists(FILE_NAME):
                    os.remove(FILE_NAME)
                    list_expenses, list_added = [], []
                    total_prices, amount_of_money = 0, 0
                    print("🗑️ Data wiped successfully.")
            
        elif option == 5:  # EXIT
            print("👋 Goodbye! Don't forget to save your progress.")
            break

if __name__ == "__main__":
    main()
