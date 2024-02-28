# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# initialliza all of the variables
total_months = 0
net_total_profit_losses = 0
last_month_profit_losses = 0
average_change = 0
monthly_changes = []
greatest_increase = ["", 0]     # month amount
greatest_decrease = ["", 99999999999999]    # month amount

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile) # csv.reader object - read the CSV file line by line.
    header = next(csvreader) # skip the header row
    
    for row in csvreader:
        # The total number of months included in the dataset
        total_months +=1
       
        # The net total amount of "Profit/Losses" over the entire period
       
        # add the total amount of "Profit/Losses"
        net_total_profit_losses += int(row[1])
        # calculate the monthly changes in "Profit/Losses"
        if total_months > 1:
            monthly_change = int(row[1]) - last_month_profit_losses # calculate the monthly change for each month
            monthly_changes.append(monthly_change) # add the monthly change to the list
           
            # find the greatest increase in profits (date and amount) over the entire period
            if monthly_change > greatest_increase[1]:
                greatest_increase = [row[0], monthly_change]
                
            # greatest decrease
            if monthly_change < greatest_decrease[1]:
                greatest_decrease = [row[0], monthly_change]
                
            
            # Update the previous month "Profit/Losses" for next iteration's change calculation
        last_month_profit_losses = int(row[1])

# Calculate the average of the changes in "Profit/Losses"
average_change = sum(monthly_changes) / len(monthly_changes)


# Print out all of the results
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# write a text file
textpath = os.path.join('analysis', 'budget_analysis.txt')
with open(textpath, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("--------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total_profit_losses}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
    
