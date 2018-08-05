import os
import csv

file_path = os.path.join('Resources','election_data.csv')
candidate_list = []
candidate_names = []
cand_dict = {}
cand_dict2 = {}
c = 0

with open(file_path) as file:
    data = csv.reader(file,delimiter=',')
    next(data)
    
    for row in data:
        candidate_list.append(row[2])
    
    candidate_s = set(candidate_list)
    for row in candidate_s:
        candidate_names.append(row)
        
total_votes =(len(candidate_list))
print("Election Results"+ "\n" +"Total votes: "+str(total_votes))   
    
for row in candidate_names:
    candidate = str(candidate_names[c])
    votes = candidate_list.count(candidate)
    votes = int(votes)
    percentage = round((votes / total_votes * 100), 3)
    cand_dict.update({ candidate : votes})
    cand_dict2.update({votes : candidate})
    print(candidate, ":  ", percentage, "%  (", votes, ")" )
    c = c+1
    
Winner = max(cand_dict.values())
print("Winner: "+str(cand_dict2[Winner]))
