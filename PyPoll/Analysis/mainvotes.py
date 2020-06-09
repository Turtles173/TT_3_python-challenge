import os
import csv

# Set the path for the file
pollingpath = os.path.join("..", "Resources", "election_data.csv")

with open(pollingpath, "r") as input_csv_file:
    csvreader = csv.reader(input_csv_file, delimiter = ",")

    # Remove the header row
    header_row = next(csvreader)

    #Table variable
    table_data = list(csvreader)

    #Count the number of votes in the dataset
    votes = str(len(table_data))

def election_results(voting):

    voterid = voting[0]
    county = voting[1]
    candidate = voting[2]

    khan = []
    for row in csvreader:
        if(name_to_check() == row[2].upper()):
            election_results(row)

       









print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
print("--------------------------")

