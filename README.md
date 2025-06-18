# 🛒 Smart Grocery Organizer – Python Project

This is a smart and simple **Python grocery management app** that lets you **add, update, list, and delete grocery items** while tracking their expiry dates. It’s designed to help users avoid wasting food and stay organized.

---

## ✅ Key Features

- ➕ Add new grocery items with quantity and expiry date
- 📋 List all saved grocery items
- ⏰ Get alerts for items expiring soon or already expired
- ❌ Remove an item by its number
- 🔁 Update the quantity of any item
- 💾 Saves all data to a local JSON file

---

## 🧠 What This App Teaches

This project helps you practice and understand:
- File handling using JSON
- Working with dates using `datetime` and `timedelta`
- User input and menu-driven apps
- List and dictionary operations in Python
- Error handling and validation

---

## 💻 How to Run

1. Make sure Python 3 is installed
2. Save the script as `smart_grocery_organizer.py`
3. Open terminal or command prompt
4. Run the script:

```bash
python smart_grocery_organizer.py
```

5. Choose any option from the menu and start managing your groceries!

---

## 📂 Data Storage

- All items are saved in a file named **`grocery_data.json`**
- It stores your list even after you close the app

Example data format:

```json
[
    {
        "name": "Milk",
        "quantity": "2 bottles",
        "expiry_date": "2025-06-20"
    }
]
```

---

## 🧪 Example Output

```text
===== 🛒 Smart Grocery Organizer =====
1. Add Grocery Item
2. List Grocery Items
3. Check Expiry Alerts
4. Remove an Item
5. Update Item Quantity
6. Exit
Choose an option (1-6): 3

⚠️ Items expiring within 3 days or already expired:
- Milk | Qty: 2 bottles | Expiry: 2025-06-20 | Expiring Soon
```

---

## 🧰 Technologies Used

- Python 3.x
- `json` module for data saving
- `datetime` for date management
- `os` for file checks
- Terminal input/output

---

## 📌 Why I Built This

This project was built to solve a simple daily life problem — **forgetting what’s in the fridge and when it expires**. It's great for learning file I/O, data management, and real-world logic.

---

## 📄 License

This project is open-source under the **MIT License**.  
You’re free to use, modify, and share it with credit.

---

## 🙋‍♂️ About Me

I'm **Ali Zain**, a Python developer and AI student passionate about building smart and helpful tools that make everyday tasks easier.

> “Code what you need, and others will need it too.”
