import os
import csv

# Set the path for the file
budgetpath = os.path.join("../Resources", "budget_data.csv")

with open(budgetpath, "r") as input_csv_file:
    csvreader = csv.reader(input_csv_file, delimiter = ",")
    
    # Remove the header row
    header_row = next(csvreader)

    #Table variable
    table_data = list(csvreader)

    #Count the number of months in the dataset
    months = str(len(table_data))

    #Add the total Profit and Losses for the period
    pandl_total = 0
    for row in table_data:
        pandl_total += int(row[1])

    #Calculate the movement for each month
    #Add a column
    #Current month - last month
        # **** change = 
    
    open_profit_move = int(row[1])
    close_profit_move = int(row-1[1])
    profit_move = int(close_profit_move -= open_profit_move)
    months_ave = int(months -= 1)
    total_profit_move = 0
    for number in table_data:
        total_profit_move += number
        return total_profit_move /= months_ave




    #What is the average change over the entire period
     
        # *** ave_change = change / (months - 1)

    #What was the month with the greatest increase in profits
        #changehigh = $$$
        #highmonth (which month)

    #What was the month with the greatest decrease in profits
        #changelow = $$$
        #lowmonth = (which month)

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {months}")
print(f"Total Profit & Loss: ${pandl_total}")
print(f"Average Change: ${total_profit_move})

#print(f"Greatest Increase in Profits: {Month2} '(${changehigh})'")
#print(f"Greatest Decrease in Profits: {Month3} '(${changelow})'")




# ------------ RESOURCES AND REFERENCES FROM USED OUTSIDE OF CLASS ACTIVITIES ------------

# https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python
