import json
from datetime import datetime

# Function to load periods from a JSON file
def load_data(filename='periods.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save periods to a JSON file
def save_data(periods, filename='periods.json'):
    with open(filename, 'w') as file:
        json.dump(periods, file)

# Function to record your periods
def record_your_periods(periods):
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    periods.append({"period_start_date": start_date, "period_end_date": end_date})
    save_data(periods)
    print("Period logged successfully!")

# Function to view your periods
def view_your_periods(periods):
    if not periods:
        print("No periods logged yet.")
    else:
        print("Logged Periods:")
        for period in periods:
            print(f"From {period['period_start_date']} to {period['period_end_date']}")

# Main function to run the app
def main():
    periods = load_data()
    while True:
        print("\nPeriod Tracker")
        print("1. Record a Period")
        print("2. View your Periods")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            record_your_periods(periods)
        elif choice == '2':
            view_your_periods(periods)
        elif choice == '3':
            print("Exiting the app.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
