import os
import csv

pybank=os.path.join("Resources","budget_data.csv")

#Months dictionary
months = []

#Profit dictionary
profitloss = []

#Change in Profit dictionary
profitchange = []

#Start point for Total Profit/Losses
total = 0

#Defined function to calculate change in monthly Profit/losses
def avgchange (startPoint,currentPoint):
    return((currentPoint)-(startPoint))

#Open and read csv
with open(pybank,newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")

    #Total the Profit/Losses column then write the Date to a dictionary and Profit/Losses to a dictionary
    for row in csvreader:
        total += float(row['Profit/Losses'])
        Date = row["Date"]
        Profit = row["Profit/Losses"]
        months.append(
            {"Date": row["Date"]
            }
        )
        profitloss.append(
           float(row["Profit/Losses"])           
        )

    #Use defined function to calculate change in monthly Profit/Losses
    for eachN in profitloss:
        change = avgchange(profitloss[0],eachN)/len(months)
        #appends list of profitloss to profitchange dictionry
        changes = avgchange(profitloss[0],eachN)
        profitchange.append(
            changes
        )
    #Set the decimal two places
    change = "%.2f" % round(change, 2)

    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${int(total)}")
    print(f"Average Change: ${(change)}")
    #I'm not sure how to capture the date for the min max.
    #print(profitchange)
    print(max(profitchange))
    print(min(profitchange))
    #print(Greatest Increase in Profits: date and dollars)
    #print(Greatest Decrease in Profits: date and dollars)

