import os # This will allow us to create file paths across operating systems
import csv # Module for reading CSV files

output_path = os.path.join('Resources','election_data.csv')
Report_path = os.path.join('Analysis','myreport.txt')
myreport = open(Report_path, 'w')



with open(output_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Variables to use
    total_votes = 0
    votes_charles = 0
    votes_diane = 0
    votes_raymon = 0
    winner = ""


    for row in csvreader:       
        total_votes = total_votes + 1

        if row[2] == "Charles Casper Stockham":
            votes_charles = votes_charles + 1
        elif row[2] == "Diana DeGette":
            votes_diane = votes_diane + 1
        else:
            votes_raymon = votes_raymon + 1

shares_charles = (votes_charles / total_votes)*100
shares_diane = (votes_diane / total_votes)*100
shares_raymon = (votes_raymon / total_votes)*100

if votes_raymon > votes_diane and votes_charles > votes_charles:
    Winner = "Raymon Anthony Doane"
elif votes_charles > votes_diane and votes_charles > votes_raymon:
    Winner = "Charles Casper Stockham"
else:
    Winner = "Diana DeGette"

    
output = f'''
Election Results
-------------------------
Total Votes: {total_votes:,}
-------------------------
Charles Casper Stockham: {shares_charles:,.3f}% ({votes_charles:,})
Diana DeGette: {shares_diane:,.3f}% ({votes_diane:,})
Raymon Anthony Doane: {shares_raymon:,.3f}% ({votes_raymon:,})
-------------------------
Winner: {(Winner)}
-------------------------
'''
print(output)

myreport.write(output)