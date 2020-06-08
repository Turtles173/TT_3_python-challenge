import os
import csv

# Set the path for the file
budgetpath = os.path.join("../Resources", "budget_data.csv")

with open(budgetpath, "rw") as input_csv_file:
    csvreader = csv.reader(input_csv_file, delimiter = ",")
    
    # Remove the header row
    header_row = next(csvreader)

    #Table variable
    table_data = 0
    table_data = list(csvreader)

    for row in csvreader:
        
    #Count the number of months in the dataset
        months = str(len(table_data)

    #Add the total Profit and Losses for the period
        #pandl = row([1])
        pandl = sum(int(x[2]) for x in budgetpath)

    #Calculate the movement for each month
    #Add a column
    #Current month - last month
        change = 

    #What is the average change over the entire period
     
        ave_change = change / (months - 1)

    #What was the month with the greatest increase in profits
        #changehigh = $$$
        #highmonth (which month)

    #What was the month with the greatest decrease in profits
        #changelow = $$$
        #lowmonth = (which month)

print('Financial Analysis')
print('--------------------------')
print(f"Total Months: {Months}")
print(f"Total Profit & Loss: ${pandl}")
print(f"Average Change: ${ave_change})
print(f"Greatest Increase in Profits: {Month2} '(${changehigh})'")
print(f"Greatest Decrease in Profits: {Month3} '(${changelow})'")
