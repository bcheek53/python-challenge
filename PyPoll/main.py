import os
import csv

pypoll=os.path.join("Resources","election_data.csv")

total = 0

#Open and read csv
with open(pypoll,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    voters = []

    county = []
    
    candidate = []

    unique_candidate = []

    castvotes = []
  
    for row in csvreader:
        
        voters.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {len(voters)}")
    print("--------------------------")

    for x in candidate: 
        # check if exists in unique_list or not 
        if x not in unique_candidate: 
            unique_candidate.append(x)
            castvotes.append(candidate.count(x))
            print(f"{(x)}: {round((candidate.count(x)/len(voters))*100,3)}% ({candidate.count(x)})")
    
    max_winner = str(unique_candidate[castvotes.index(max(castvotes))])       
    
    print("--------------------------")
    print(f"Winner: {max_winner}")
    
