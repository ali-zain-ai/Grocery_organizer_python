import json
from datetime import datetime, timedelta
import os

DATA_FILE = "grocery_data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_item():
    name = input("Enter item name: ").strip()
    qty = input("Enter quantity: ").strip()
    expiry = input("Enter expiry date (YYYY-MM-DD): ").strip()

    # Validate expiry date
    try:;
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format!")
        return

    data = load_data()

    # Add item dict
    item = {
        "name": name,
        "quantity": qty,
        "expiry_date": expiry
    }

    data.append(item)
    save_data(data)
    print(f"✅ Item '{name}' added successfully.\n")
    
def list_items():
    data = load_data()
    if not data:
        print("📭 No items in your grocery list.\n")
        return

    print("\n🛒 Grocery Items:")
    for i, item in enumerate(data, start=1):
        print(f"{i}. {item['name']} - Qty: {item['quantity']} - Expiry: {item['expiry_date']}")
    print()

def check_expiry():
    data = load_data()
    if not data:
        print("📭 No items to check expiry.\n")
        return

    today = datetime.now()
    soon = today + timedelta(days=3)

    print("\n⚠️ Items expiring within 3 days or already expired:")
    alert_found = False
    for item in data:
        expiry_date = datetime.strptime(item['expiry_date'], "%Y-%m-%d")
        if expiry_date <= soon:
            alert_found = True
            status = "EXPIRED" if expiry_date < today else "Expiring Soon"
            print(f"- {item['name']} | Qty: {item['quantity']} | Expiry: {item['expiry_date']} | {status}")
    if not alert_found:
        print("No items expiring soon.\n")
    else:
        print()

def remove_item():
    data = load_data()
    if not data:
        print("📭 No items to remove.\n")
        return

    list_items()
    try:
        idx = int(input("Enter item number to remove: "))
        if 1 <= idx <= len(data):
            removed = data.pop(idx-1)
            save_data(data)
            print(f"🗑️ Removed item '{removed['name']}' successfully.\n")
        else:
            print("❌ Invalid item number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def update_quantity():
    data = load_data()
    if not data:
        print("📭 No items to update.\n")
        return

    list_items()
    try:
        idx = int(input("Enter item number to update quantity: "))
        if 1 <= idx <= len(data):
            new_qty = input(f"Enter new quantity for '{data[idx-1]['name']}': ").strip()
            data[idx-1]['quantity'] = new_qty
            save_data(data)
            print(f"✅ Quantity updated for '{data[idx-1]['name']}'.\n")
        else:
            print("❌ Invalid item number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def menu():
    print("===== 🛒 Smart Grocery Organizer =====")
    print("1. Add Grocery Item")
    print("2. List Grocery Items")
    print("3. Check Expiry Alerts")
    print("4. Remove an Item")
    print("5. Update Item Quantity")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    return choice
def main():
    while True:
        choice = menu()
        if choice == '1':
            add_item()
        elif choice == '2':
            list_items()
        elif choice == '3':
            check_expiry()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            update_quantity()
        elif choice == '6':
            print("👋 Thanks for using Smart Grocery Organizer!")
            break
        else:
            print("❌ Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
