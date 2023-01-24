import os
import csv
from pathlib import Path 

# csvpath = Path('/Users/majosegarciamontes/Desktop/election_data.csv')

BallotID_count_votes = 0
Candidates = []
Dictionary_Candidatecount_votes = {}
WinningCandidate = ""
WinningCountTracker = 0
WinningPercentage = 0

with open(csvpath) as csvfile:
    cvsreader = csv.reader(csvfile,delimiter=",")
    headers = next(cvsreader)
    
    for row in cvsreader:
        BallotID_count_votes += 1
        candidateName_eachRow = row[2]

        if candidateName_eachRow not in Candidates: 
            Candidates.append(candidateName_eachRow)
            Dictionary_Candidatecount_votes[candidateName_eachRow] = 0
        
        Dictionary_Candidatecount_votes[candidateName_eachRow] += 1

    Election_Results = (
        f"\nElection results\n"
        f"\n"
        f"------------------------------\n"
        f"\n"
        f"Total votes: {BallotID_count_votes}\n"
        f"\n"
        f"------------------------------\n"
        f"\n")
    print(Election_Results, end="")
   

    for candidateName_eachRow in Dictionary_Candidatecount_votes: 
        count_votes = Dictionary_Candidatecount_votes[candidateName_eachRow]
        
        
        VotePercentage = float(count_votes) / float(BallotID_count_votes) * 100
        results = (f" {candidateName_eachRow}: {VotePercentage:.3f}% ({count_votes})\n")
        print(results)
        
     
        if (count_votes > WinningCountTracker) and (VotePercentage > WinningPercentage): 
            
            WinningCountTracker = count_votes 
            WinningCandidate = candidateName_eachRow

    WinningCandidate_summary = (
        f"------------------------------\n"
        f"\n"
        f"Winner: {WinningCandidate}\n"
        f"\n"
        )
    print(WinningCandidate_summary)
    
analysis_file = Path('/Users/majosegarciamontes/Desktop/Challenge3/pypoll/PyPoll_Majo.txt')

with open(analysis_file,"w") as file:
    file.write(f" {(Election_Results)}")
    for candidateName_eachRow in Dictionary_Candidatecount_votes: 
        count_votes = Dictionary_Candidatecount_votes[candidateName_eachRow]
        VotePercentage = float(count_votes) / float(BallotID_count_votes) * 100
        results = (f" {candidateName_eachRow}: {VotePercentage:.3f}% ({count_votes})\n")
        file.write(results)
    file.write(f"{WinningCandidate_summary}")