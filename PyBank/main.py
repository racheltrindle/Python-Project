import os
import csv 
csvpath = os.path.join("budget_data.csv")
with open (csvpath, newline="") as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    # csv_header = next (csvfile)
    # print(f"Header: {csv_header}")
    column1, column2 = [],[]
    for row in data:
        column1.append([row[0]])
        column2.append([row[1]])
        # column1 = [row[0] for row in data]
        # column2 = [row[1] for row in data]
    print (column1)
    print (column2)

#The net total amount of "Profit/Losses" over the entire period
# with open (budget_data.txt) as f:
#     reader=csv.DictReader(f)
#     for row in reader:
#             for (a,b) in row.items():
#                 columns[a].append(b)
# print(columns['date'])
# print (column['profit/loss']


#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period  
#The total number of months included in the dataset
#final grid  
# row_count = sum(1 for row in csvfile)
# print("Total Months: " + str(row_count))  
# total = 10000
# print ("Total: $" + str(total))
# AverageChange = -5000
# print ("Average Change:" + str(AverageChange))
# GreatestIncreaseMonth= "Feb-2012"
# GreatestInreaseAmount = 9999
# print ("Greatest Increase in Profits:" + str(GreatestIncreaseMonth) + "(" + str(GreatestInreaseAmount) + ")")
# GreatestDecreaseMonth= "Sep-2013"
# GreatestDecreaseAmount = 7777
# print ("Greatest Decrease in Profits:" + str(GreatestDecreaseMonth) + "(" + str(GreatestDecreaseAmount) + ")")