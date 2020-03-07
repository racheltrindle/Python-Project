import os
import csv 
budget_csv = os.path.join("budget_data.csv")
py= open("budget_data.csv","r")
csv_py = csv.reader(py)
csv_header=next(csv_py)
with open ("budget_data.csv","r") as f:
    headerline = f.readline ()
    data = csv_py
    next(data, None)
    total = 0
    for row in csv.reader(f):
        total += int(row[1])
    print("Financial Analysis")
    print ("------------------")
    print ("Total: $" + str(total))
    total_months = sum(1 for row in csv_py)+1
    print ("Total months: " + str(total_months))  
    print ("Average change: ")
    print ("Greatest increase in profits: ")
    print ("Greatest Decease in profits : ") 

# What I tried to do 
#1. Make each column into a list and assign variable, dates=[0]; values=[1]
#2. Use max/min function to retrieve the max numbers from those lists
#3. For average change - wanted to say when for each value in dates list, 
#to calculate the output in the values column to get each amount, then total and divide by rowcount.

# I tried multiple ways to find max value and just kept getting the last number in the column

   
    # values = row[1]
    # for rows in values:
    #     values += max(row[1])
    #     print (values)

# with open ("budget_data.csv", "r") as csvfile:
#     lines = csvfile.readlines()
#     list=[]
#     for line in lines:
#         data = line.split(',')
#     dates.append(data[0])
#     budget.append(data[1])
# def percentchange(startpoint,currentpoint):
#     return(((currentpoint)-startpoint)/abs(startpoint))*100
# for line in list:
#     pc=percentchange(dates,budget)
#     print (dates)

# high_val= max ((data),key=lambda _: _[1])
    # print(high_val)
    # maxnum = max(csv_py, key=lambda row: int(row[1]))
    # print(maxnum)

# word_counter = Counter(values)
# print(word_counter)
