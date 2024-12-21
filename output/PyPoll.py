#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
import os 

election_csv = r"/Users/katigbakv/Desktop/module-3-re/PyPoll/Resources/election_data.csv"

total_votes = 0
candidate_votes = {}


with open(election_csv, mode='r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    

    for row in csvreader:
        total_votes += 1  
        candidate = row[2] 
        
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

winner = max(candidate_votes, key=candidate_votes.get)  


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


output_file = r"/Users/katigbakv/Desktop/module-3-re/output/election_results.txt"


with open(output_file, mode='w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")


# In[ ]:




