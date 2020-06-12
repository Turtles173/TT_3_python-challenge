import os
import csv

# Set the path for the file
budgetpath = os.path.join("..", "Resources", "budget_data.csv")

with open(budgetpath, "r", encoding = 'utf8') as input_csv_file:
    csvreader = csv.reader(input_csv_file, delimiter = ",")
    
    
    # Remove the header row
    header_row = next(csvreader)

    #Table variable
    table_data = list(csvreader)

    #Count the number of months in the dataset
    total_months = str(len(table_data))

    #Add the total Profit and Losses for the period
    pandl_total = 0
    for row in table_data:
        pandl_total += int(row[1])

    #Calculate the movements for each month
    with open(budgetpath, "r") as input_csv_file:
        lines = input_csv_file.readlines()
    data_budget = []
    for line in lines[1:]: #Google-Fu moment here - don't read the first line containing month and amount
        line = line.strip("\n") #Google-Fu moment here - erase the newline character from each line
        data_budget.append(line.split(",")) #Google-Fu moment here - split the lines using the comma as a delimiter
    output = []
    for index,month_after in enumerate(data_budget[1:]): #Google-Fu moment here - start in the month after the previous month to subtract the first one
        output.append(int(month_after[1])-int(data_budget[index][1]))
    average = sum(output) / len(output)
    max_move = max(output)
    min_move = min(output)
    
    #Match the month to the max_move and min_move
    
    high_index = output.index(max_move)
    low_index = output.index(min_move)
    high_month = data_budget[high_index + 1][0]
    low_month = data_budget[low_index + 1][0]


print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit & Loss: ${pandl_total}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {high_month}  (${max_move})")
print(f"Greatest Decrease in Profits: {low_month}  (${min_move})")

#Export the file to a new text

with open("budget_export.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("--------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total Profit & Loss: ${pandl_total}\n")
    text_file.write(f"Average Change: ${average:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {high_month}  (${max_move})\n")
    text_file.write(f"Greatest Decrease in Profits: {low_month}  (${min_move})\n")



# ------------ RESOURCES AND REFERENCES FROM USED OUTSIDE OF CLASS ACTIVITIES ------------

# https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python
# https://stackoverflow.com/questions/59494280/loop-over-csv-and-subtract-previous-line-from-current-line
# https://stackoverflow.com/questions/23019773/locate-the-index-of-largest-value-in-an-array-python
# https://stackoverflow.com/questions/5214578/print-string-to-text-file


