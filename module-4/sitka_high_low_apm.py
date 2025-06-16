#Alexis Mitchell
#June 15, 2025
# By user's choice, this program graphs the highs and low of temperatures
# from the 2018 sitka weather csv file

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

# Load data once at start
filename = 'sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, highs, and lows from file
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            # Skipping missing or malformed data
            print(f"Missing data for {row[2]}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Program loop
while True:
    print("\nWeather Data Menu:")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        # Plot highs
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == '2':
        # Plot lows
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == '3':
        print("Exiting...")
        sys.exit()

    else:
        print("Invalid input. Please enter 1, 2, or 3.")