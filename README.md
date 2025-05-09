﻿# 💰 MoneyTracker – Personal Finance Manager

MoneyTracker is a simple personal finance app that helps you track income and expenses, visualize transactions, and manage your budget – all from a clean Python interface with a Tkinter-based GUI.

## Features

- Add income and expense transactions
- Auto-save to CSV files
- Filter transactions by category and type
- Visualize income/expenses over time
- GUI with date, category, amount input and checkbox for income
- Automatically stores transaction dates
- View current balance and highest transactions

## 🖥️ GUI Preview

![GUI Preview](assets/gui.png)

## 🚀 Getting Started

### Prerequisites

Make sure Python 3.9+ is installed, then install dependencies:

```bash
pip install pandas matplotlib

Run the app

python gui.py

Or just run tracker.py for CLI interactions.
📁 Project Structure

.
├── tracker.py         # Core finance logic
├── gui.py             # GUI application (Tkinter)
├── test_finances.csv  # Auto-generated finance records
├── assets/            # Optional: screenshots or icons
└── README.md

🛠️ To-Do

Add budget limits by category

Export to Excel

Add dark/light theme toggle

    Category pie chart visualization

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Created by Pedro Heringer
