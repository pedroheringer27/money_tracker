import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from tracker import MoneyTracker

class MoneyTrackerGUI:
    def __init__(self, master, tracker):
        self.master = master
        self.master.title("Money Tracker")
        self.master.geometry("500x600")
        
        self.tracker = tracker

        # Transaction input fields
        self.category_label = tk.Label(self.master, text="Category:")
        self.category_label.pack(pady=5)
        self.category_entry = tk.Entry(self.master)
        self.category_entry.pack(pady=5)
        
        self.amount_label = tk.Label(self.master, text="Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack(pady=5)
        
        self.type_label = tk.Label(self.master, text="Type:")
        self.type_label.pack(pady=5)
        self.type_var = tk.StringVar()
        self.type_var.set("Income")  # Default value
        self.type_menu = tk.OptionMenu(self.master, self.type_var, "Income", "Expense")
        self.type_menu.pack(pady=5)
        
        self.add_button = tk.Button(self.master, text="Add Transaction", command=self.add_transaction)
        self.add_button.pack(pady=10)
        
        # Balance display
        self.balance_label = tk.Label(self.master, text="Balance: $0")
        self.balance_label.pack(pady=10)
        
        # Category filter
        self.filter_label = tk.Label(self.master, text="Filter by Category:")
        self.filter_label.pack(pady=5)
        self.filter_entry = tk.Entry(self.master)
        self.filter_entry.pack(pady=5)
        self.filter_button = tk.Button(self.master, text="Filter", command=self.filter_by_category)
        self.filter_button.pack(pady=5)
        
        # Checkboxes for Income and Expense
        self.show_income = tk.BooleanVar()
        self.show_expense = tk.BooleanVar()
        self.income_checkbox = tk.Checkbutton(self.master, text="Show Income Transactions", variable=self.show_income)
        self.income_checkbox.pack(pady=5)
        self.expense_checkbox = tk.Checkbutton(self.master, text="Show Expense Transactions", variable=self.show_expense)
        self.expense_checkbox.pack(pady=5)

        # Graph summary buttons
        self.graph_button = tk.Button(self.master, text="Show Income Graph", command=self.show_graph)
        self.graph_button.pack(pady=10)
        
        self.update_balance()

    def add_transaction(self):
        category = self.category_entry.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid number for the amount.")
            return
        t_type = self.type_var.get()

        # Add the transaction to the tracker
        self.tracker.add_transaction(category, amount, t_type)
        self.update_balance()
        messagebox.showinfo("Success", "Transaction added successfully!")
        
    def filter_by_category(self):
        category = self.filter_entry.get()
        filtered_data = self.tracker.filter_by_category(category)
        messagebox.showinfo("Filtered Data", filtered_data.to_string())
        
    def update_balance(self):
        balance = self.tracker.balance()
        self.balance_label.config(text=f"Balance: {balance}")

    def show_graph(self):
        if self.show_income.get():
            self.tracker.plot_summary("Income")
        if self.show_expense.get():
            self.tracker.plot_summary("Expense")
        

# Create an instance of your MoneyTracker class
tracker = MoneyTracker("test_finances")

# Set up the Tkinter window
root = tk.Tk()
gui = MoneyTrackerGUI(root, tracker)

root.mainloop()