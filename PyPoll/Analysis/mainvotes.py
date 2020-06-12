import os
import csv
from collections import Counter


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
    
    #print(candidate_names)

    #Add the votes per candidate
    candidate_count = Counter()
    for prospect_name in candidate_names:
        candidate_count[prospect_name] += 1

    print(candidate_count)
    
    #Calculate the percentage of each candidate
    percent = (candidate_count / total_votes) * 100

    print(percent)
    
    
    
    
    
 



print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
# print(f"TEsting: {vote_count}")
# print(f"TEsting2: {number_of_votes}")



#Write results to a new text file

#"\n" is added to create a new line after each entry

#text_file = open("Polling_Vote.txt", "w")

#with open("Polling_Vote.txt", "w") as text_file:


# text_file.close()



#-----------------REFERENCES -------------------

# https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
# https://www.programiz.com/python-programming/methods/list/append
# https://realpython.com/python-zip-function/





# TEsting code to hold

#First try at getting names to help with the logic
    # cand = ["Khan", "Correy", "Li", "O'Tooley"]

    # for row in table_data:
    #     cand.append(row[2])
        
    # candidate_count = Counter(cand)
