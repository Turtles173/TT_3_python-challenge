import os
import csv

# Set the path for the file
budgetpath = os.path.join("..", "Resources", "budget_data.csv")

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
    #Current month - last month
    with open(budgetpath, "r") as input_csv_file:
        lines = input_csv_file.readlines()
    data = []
    for line in lines[1:]: #don't read the first line containing month and amount
        line = line.strip("\n") #erase the newline character from each line
        data.append(line.split(",")) #split the lines using the comma as a delimiter

    output = []
    for index,element in enumerate(data[1:]): #we start in the second element because we will subtract the first one
        output.append(int(element[1])-int(data[index][1]))

    average = sum(output) / len(output)

    



print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {months}")
print(f"Total Profit & Loss: ${pandl_total}")
print(f"Average Change: ${average}")


#print(f"Greatest Increase in Profits: {Month2} '(${changehigh})'")
#print(f"Greatest Decrease in Profits: {Month3} '(${changelow})'")




# ------------ RESOURCES AND REFERENCES FROM USED OUTSIDE OF CLASS ACTIVITIES ------------

# https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python
# https://stackoverflow.com/questions/59494280/loop-over-csv-and-subtract-previous-line-from-current-line
# https://stackoverflow.com/questions/23019773/locate-the-index-of-largest-value-in-an-array-python

