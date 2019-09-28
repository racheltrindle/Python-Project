import os
import csv 
csvpath = os.path.join("budget_data.csv")
with open (csvpath, newline="") as csvfile:
    row_count = sum (1 for row in csvfile) - 1
    net_total = csv.reader(open("budget_data.csv","r"))
    next(net_total)
    numbers = (float(row[1]) for row in net_total)
    total = sum(numbers)
    ave_columns = ((total)/((86*2))/100)
print ("Total: $" + str(total))
print("Total Months: " + str(row_count))
print (ave_columns)


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