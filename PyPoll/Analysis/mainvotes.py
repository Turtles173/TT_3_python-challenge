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

    #Candidate list for the moment - need to automate
    cand_list = ["Khan", "Correy", "Li", "O'Tooley"]
    
    vote_count = cand_list.count("Khan")
    
    
    number_of_votes = 0
    for cand_list in table_data:
        number_of_votes = str(cand_list[2])


    
    # def election_results(voting):
    #voterid = table_data[0]
    #county = table_data[1]
    #candidate = table_data[2]



#     khan = []
#     for row in csvreader:
#         if(name_to_check() == row[2].upper()):
#             election_results(row)

    








print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
print("--------------------------")
print(f"TEsting: {vote_count}")
print(f"TEsting2: {number_of_votes}")

