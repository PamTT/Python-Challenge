#MainPy
#The total number of votes cast


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.

import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

#The total number of votes cast
number_of_votes=0
with open (csvpath,'r') as csv_file:
    csv_reader_object = csv.reader(csv_file)
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        number_of_votes = number_of_votes+1
        csv_reader_object.line_num
    

#A complete list of candidates who received votes
list_candidates = []
candidates_and_votes =[]
with open (csvpath,'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    data=[row for row in csv_reader]
    [list_candidates.append(row[2])
    for row in data if row[2] not in list_candidates]
    
    candidates_and_votes.append((len(candidates_and_votes)))
    candidates_and_votes=[]
    #print(candidates_and_votes)


print('----------------')
print('Election Results')
print('Total votes = ' +str(number_of_votes-1))
print('----------------')
print(list_candidates)
#print("votes per candidates")






