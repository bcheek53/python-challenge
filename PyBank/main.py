import os
import csv

pybank=os.path.join("Resources","budget_data.csv")

#Open and read csv
with open(pybank,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    #Months dictionary
    months = []

    #Profit dictionary
    profitloss = []
    
    #Change in Profit dictionary
    profitchange = []

    #Total the Profit/Losses column then write the Date to a dictionary and Profit/Losses to a dictionary
    for row in csvreader:
        
        months.append(row[0])
        profitloss.append(float(row[1]))

    #appends list of profitloss to profitchange dictionry
    for i in range(1,len(profitloss)):
        profitchange.append(profitloss[i] - profitloss[i-1])
        #calculates average change
        changes = round(sum(profitchange)/len(profitchange),2)

        max_change = max(profitchange)
        max_date = str(months[profitchange.index(max(profitchange))+1])
        min_change = min(profitchange)
        min_date = str(months[profitchange.index(min(profitchange))+1])

    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${int(sum(profitloss))}")
    print(f"Average Change: ${(changes)}")
    print(f"Greatest Increase in Profits: {max_date} (${int(max_change)})")
    print(f"Greatest Decrease in Profits: {min_date} (${int(min_change)})")

fh = open("pybank.txt", "w")

fh.write("Financial Analysis\n"
        "-------------------------------\n"
        f"Total Months: {len(months)}\n"
        f"Total: ${int(sum(profitloss))}\n"
        f"Average Change: ${(changes)}\n"
        f"Greatest Increase in Profits: {max_date} (${int(max_change)})\n"
        f"Greatest Decrease in Profits: {min_date} (${int(min_change)})")

fh.close()
