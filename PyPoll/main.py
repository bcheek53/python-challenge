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


  
    for row in csvreader:
        
        voters.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    

    for x in candidate: 
        # check if exists in unique_list or not 
        if x not in unique_candidate: 
            unique_candidate.append(x) 
            print(candidate.count(x))



print("Election Results")
print("--------------------------")
print(f"Total Votes: {len(voters)}")
print("--------------------------")