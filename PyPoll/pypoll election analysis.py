#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

pypoll_csv = os.path.join('.', 'Resources', 'election_data.csv')
output_file = os.path.join('.', 'election_analysis.txt')

total_votes = 0

candidate_votes = {}
candidate_options = []

winning_candidate = ""
winning_count = 0

with open(pypoll_csv) as election_data:
    
    reader = csv.reader(election_data, delimiter=',')
    header = next(reader)  
    
   
    for row in reader:
        
        # calculate total votes
        total_votes += 1
        
        # determine the candidates by adding the name to the candidate_options list if the list does not contain any existing candidate
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name]+= 1

with open(output_file, 'w') as txt_file:
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n"
    )
    print(election_results)
    
    txt_file.write(election_results)
    
    # calculate the vote percentage for each candidate and determine the winning candidate
    
    for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            
            # calculate the vote percentage for each candidate
            vote_percentage = float(votes) / float(total_votes) * 100
            
            # determine winning candidate
            if(votes > winning_count):
                winning_count = votes
                winning_candidate = candidate
            
            # output of each candidate with the vote percentage and number of votes
            voter_output= f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            
            print(voter_output, end="")
            
            txt_file.write(voter_output)
    winning_candidate_summary = (
        "-------------------------\n"
        f"Winner: {winning_candidate}\n"
        "-------------------------"
    )
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)


# In[ ]:




