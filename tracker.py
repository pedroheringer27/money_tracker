import os
import pandas as pd
import matplotlib.pyplot as plt

class MoneyTracker:
    # Access the file
    def __init__(self, file):
        self.file = f"{file}.csv"
        self.data = self.load_data()
        
    def load_data(self):
        """
        Loads the data into the self.data, to have the DataFrame inside updated.
        """
        if os.path.exists(self.file):
            data = pd.read_csv(self.file, parse_dates=["Date"])
            data = data.set_index("Date")
            return data
        else:
            return pd.DataFrame(columns=["Date", "Category", "Amount", "Type"]).set_index("Date")

    # Adds a transaction to the tracker
    def add_transaction(self, category, amount, t_type):
        """
        Adds a transaction to the tracker.
        Parameters:
        category = (str) The category of the transaction.
        amount = (float) The amount of the transaction.
        t_type = (str) Type of the transaction, 'Income' or 'Expense'
        """
        if not isinstance(self.file, str):
            raise ValueError("The argument 'file' should be passed as string.")
        
        elif not isinstance(amount, (int, float)):
            raise ValueError("The amount should be passed as a float.")
        
        elif amount <= 0:
            raise ValueError("The amount has to be a positive number.")
        
        elif t_type.title() not in ["Income", "Expense"]:
            if t_type in "Expense":
                raise ValueError("The transaction type must be 'Income' or 'Expense' \nDid you mean 'Expense'?")
            elif t_type in "Income":
                raise ValueError("The transaction type must be 'Income' or 'Expense' \nDid you mean 'Income'?")
            else:
                raise ValueError("The transaction type must be 'Income' or 'Expense'.")
            
        else:
            date = pd.Timestamp.now().date()
            new_row = pd.DataFrame([[date, category, round(amount, 2), t_type.title()]], columns=['Date', 'Category', 'Amount', 'Type'])
            self.data = pd.concat([self.data, new_row.set_index("Date")])

            if os.path.exists(self.file):
                new_row.to_csv(self.file, mode='a', index=False, header=False, encoding='utf-8')
            else:
                new_row.set_index("Date", inplace=True)
                new_row.to_csv(self.file, mode='w', index=False, header=True, encoding='utf-8')
            return "Transaction saved!"

    def balance(self):
        """
        Calculates the balance of the account
        """
        total_income = self.data[self.data["Type"] == "Income"]["Amount"].sum()
        total_expended = self.data[self.data["Type"] == "Expense"]["Amount"].sum()
        return f"Your balance is {total_income - total_expended}"

    def highest_transaction(self, t_type, month=0):
        """
        Returns the most expensive or the highest income transaction
        Parameters:
        t_type = (str) Type of transaction that will return, 'Income' or 'Expense'
        """
        filtered = self.data[self.data["Type"] == t_type]

        if month != 0:
            filtered = filtered[filtered.index.month == month]

        if filtered.empty:
            return f"No {t_type} transactions found."

        highest_amount = filtered["Amount"].max()
        highest = filtered[filtered["Amount"] == highest_amount]
        return f"The highest {t_type.lower()} transaction(s):\n{highest}"
    
    def transaction_summary(self, t_type, frequency='ME'):
        """
        Returns the expense or income per the range(year, month, week), naturally returns the monthly value
        """
        summary = self.data[self.data["Type"] == t_type]["Amount"].resample(frequency).sum()
        return summary
    
    def plot_summary(self, t_type, frequency='ME'):
        """
        Creates a graph of the transaction summary
        """
        summary = self.transaction_summary(t_type, frequency)
        summary.plot(kind='bar', title=f"{t_type} over time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.tight_layout()
        plt.show()

