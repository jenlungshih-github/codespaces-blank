import pandas as pd
import os

def analyze_excel():
    """Prompts the user to enter a local Excel file path and analyzes it."""

    file_path = input("Enter the path to the Excel file: ")
    
    # Construct the absolute path relative to the current working directory
    current_directory = os.getcwd()
    absolute_path = os.path.join(current_directory, file_path)

    try:
        df = pd.read_excel(absolute_path, engine='openpyxl')
        print("\nExcel file loaded successfully!")
        print(df.head())  # Display the first few rows

        while True:
            choice = input("\nWhat would you like to do? \n1. View data \n2. Calculate summary statistics \n3. Exit \n")

            if choice == '1':
                print(df)
            elif choice == '2':
                print(df.describe())
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_excel()
