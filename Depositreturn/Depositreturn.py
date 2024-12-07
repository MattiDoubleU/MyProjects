# Author: Matthias Wiedemann

import pandas as pd
from datetime import datetime
import os

# File name for storing the data
FILE_NAME = "money_data.csv"

# Function to load data from the CSV file
def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME, parse_dates=["Date"])
    else:
        return pd.DataFrame(columns=["Amount", "Date"])

# Function to save data to the CSV file
def save_data(df):
    df.to_csv(FILE_NAME, index=False)

# Function to add an entry
def add_entry(df):
    amount = float(input("Enter amount of money: "))
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return df
    new_entry = pd.DataFrame({"Amount": [amount], "Date": [date]})
    df = pd.concat([df, new_entry], ignore_index=True)
    save_data(df)
    print("Entry added successfully.")
    return df

# Function to display the table
def display_table(df):
    if df.empty:
        print("No data to display.")
        return
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
    print("\nData Table:")
    print(df)

# Main program loop
def main():
    df = load_data()
    while True:
        print("\nOptions:")
        print("1. Add a new entry")
        print("2. Display all entries")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            df = add_entry(df)
        elif choice == "2":
            display_table(df)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main program
if __name__ == "__main__":
    main()