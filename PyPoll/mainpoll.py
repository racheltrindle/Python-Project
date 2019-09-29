import os
import csv
poll_data=os.path.join("election_data.csv")
with open (poll_data,newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    for rows in csvreader:
        total_voters=sum(1 for row in csvfile)+1
        print (total_voters)
        candidates = rows[2]
        while rows[2]==rows[2]:
            print (candidates)
            StopIteration
            