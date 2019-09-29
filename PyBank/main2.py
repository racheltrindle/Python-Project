import os
import csv 
budget_csv = os.path.join("budget_data.csv")
py= open("budget_data.csv","r")
csv_py = csv.reader(py)
csv_header=next(csv_py)

with open ("budget_data.csv") as fin:
    headerline = fin.readline ()
    total = 0
    for row in csv.reader(fin):
        total += int(row[1])
    print (total)

total_months = sum(1 for row in csv_py) 
print (total_months)   



  
