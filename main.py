import csv
import sys
from collections import defaultdict
from datetime import datetime, timedelta

if len(sys.argv) < 2:
    print("Usage: python3 main.py path/to/data.csv")
    sys.exit(1)

csv_file = sys.argv[1]

data = []
with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    
    # If the CSV has a header row, uncomment next line to skip it:
    # next(reader)
    
    for row in reader:
        # Debug: print each raw row
        print("Raw row:", row)
        
        # Skip rows that don't have exactly 3 columns
        if len(row) != 3:
            print("Skipping (invalid column count).")
            continue
        
        start_str, end_str, total_str = row
        
        # Remove any dollar signs or commas before converting to float
        cleaned_total_str = (
            total_str.strip()         # remove extra whitespace
                     .strip('"')      # remove surrounding quotes if present
                     .replace('$', '') # remove dollar sign
                     .replace(',', '') # remove commas
        )
        
        try:
            total = float(cleaned_total_str)
        except ValueError:
            print(f"Skipping (cannot parse total '{total_str}').")
            continue  # Skip rows with non-numeric totals

        try:
            start_date = datetime.strptime(start_str.strip(), "%Y-%m-%d")
            end_date = datetime.strptime(end_str.strip(), "%Y-%m-%d")
        except ValueError:
            print(f"Skipping (invalid date format) for row: {row}")
            continue  # Skip rows with invalid date formats

        if start_date > end_date:
            print(f"Skipping (start date after end date): {row}")
            continue  # Skip invalid ranges

        # Calculate the number of days (inclusive) and compute daily rate
        num_days = (end_date - start_date).days + 1
        daily_rate = total / num_days

        # Append the valid entry to data
        data.append((start_date, end_date, daily_rate))

# print("\nLoaded data:")
# for row in data:
#     print(row)

# Create event points: add the daily rate on start date, subtract on day after end date.
events = []
for start_date, end_date, daily_rate in data:
    events.append((start_date, daily_rate))
    events.append((end_date + timedelta(days=1), -daily_rate))

# Sort events by date
events.sort()

# print("\nEvents:")
# for event in events:
#     print(event)

# Use a sweep line algorithm to compute monthly totals
monthly_totals = defaultdict(float)
running_rate = 0.0
previous_date = None

for date, rate_change in events:
    if previous_date is not None:
        current_date = previous_date
        # Accumulate daily contributions until the next event
        while current_date < date:
            month_key = current_date.strftime("%Y-%m")
            monthly_totals[month_key] += running_rate
            current_date += timedelta(days=1)
    running_rate += rate_change
    previous_date = date

sumTotal = 0
# Print the monthly totals
print("\nMonthly Totals:")
if not monthly_totals:
    print("No data processed or valid dates not found.")
else:
    for month in sorted(monthly_totals.keys()):
        print(f"{month}: {monthly_totals[month]:.2f}")
        sumTotal = sumTotal + monthly_totals[month]

print(f"Sum Total {sumTotal}")
