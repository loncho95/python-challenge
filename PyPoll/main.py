import os # This will allow us to create file paths across operating systems
import csv # Module for reading CSV files

output_path = os.path.join('Resources','election_data.csv')
# Report_path = os.path.join('Analysis','myreport.txt')
# myreport = open(Report_path, 'w')



with open(output_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Variables to use


    for row in csvreader:  
        total_votes = 0
        candidate_options = []
        candidate_votes = {}  
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_options: # if the candidate does not match any existing candidate 
            candidate_options.append(candidate_name) # add it to the list of candidates
            candidate_votes[candidate_name] = 0 # tracking of the votes 
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1 # add the vote to the candidates count

for candidate in candidate_votes:
    votes  = candidate_votes.get(candidate)

print(votes)

    
# output = f'''
# Election Results
# -------------------------
# Total Votes: {total_votes:,}
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
# '''
# print(output)

print(candidate_options)