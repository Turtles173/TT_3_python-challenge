import os
import csv
from collections import Counter
import itertools


# Set the path for the file
pollingpath = os.path.join("..", "Resources", "election_data.csv")

with open(pollingpath, "r") as input_csv_file:
    csvreader = csv.reader(input_csv_file, delimiter = ",")

    # Remove the header row
    header_row = next(csvreader)

    #Table variable
    table_data = list(csvreader)

    #Count the total number of votes in the dataset
    total_votes = str(len(table_data))

    #Get the list of candidtates
    candidate_names = []
    for row in table_data:
        candidate_names.append(row[2])
    
    #Add the votes per candidate
    candidate_count = Counter()
    for prospect_name in candidate_names:
        candidate_count[prospect_name] += 1

    #Find the winner!
    winner = 1
    winner_name = dict(itertools.islice(candidate_count.items(), winner))
    
    #PERCENTAGE - haven't been able to extract the data from the dictionary 
    #from the counter - I have spent a long time on that problem!  see below 
    #just a couple of examples. I was going to insert it into the print below 
    #as required.  That bit was straight forward.


print("ELECTION RESULTS")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for print_details in candidate_count:
    print("{}: {}".format(print_details,candidate_count[print_details]))
print("--------------------------")
print(f"Winner in a landslide: {winner_name}")

#Export the file to a new text

with open("polling_export.txt", "w") as text_file:
    text_file.write("ELECTION RESULTS\n")
    text_file.write("--------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("--------------------------\n")
    for print_details in candidate_count:
        text_file.write("{}: {}\n".format(print_details,candidate_count[print_details]))
    text_file.write("--------------------------\n")
    text_file.write(f"Winner in a landslide: {winner_name}")


#-----------------COMMENTS AND IDEAS -------------------
#-------------------- RE PERCENTAGE --------------------
#---------------PLEASE PROVIDE FEEDBACK-----------------

    #convert the counter/dictionary to a list
    
    #Calculate the percentage for each candidate
    
    # percentage = []
    # for perc_calc in candidate_count[1]:
    #      percentage.append(int(perc_calc/total_votes) * 100
    
    # votes_to_ints = int(total_votes)
    # percent = cand_final_votes / total_votes * 100



#-----------------REFERENCES -------------------

# https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
# https://www.programiz.com/python-programming/methods/list/append
# https://realpython.com/python-zip-function/
# https://docs.python.org/3/library/functions.html#zip
# https://www.codevscolor.com/python-print-key-value-dictionary/



