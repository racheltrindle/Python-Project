import os
import csv 
csvpath = os.path.join("budget_data.csv")
with open (csvpath, newline="") as csvfile:
    value_sum=0
    for row in csv.reader(csvfile, delimiter=","):
        value_sum += row[2]
            print (value_sum)

#The net total amount of "Profit/Losses" over the entire period
# with open (budget_data.txt) as f:
#     reader=csv.DictReader(f)
#     for row in reader:
#             for (a,b) in row.items():
#                 columns[a].append(b)
# print(columns['date'])
# print (column['profit/loss']

# total = 0
# with open (csvpath, newline="") as csvfile:
#     for row in csv.reader(csvfile, delimiter=","):
#         for col in row:
#             total+= len(col)
#             print(total)
        
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