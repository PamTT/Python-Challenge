#MainPy
#The total number of votes cast


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.

import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
outpath = os.path.join('Analysis', 'election_result.txt')

number_of_votes=0
candidate_list = []
candidate_and_his_votes ={}


with open (csvpath,'r') as csv_file:
    
    csv_reader = csv.reader(csv_file,delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        #Find total number of vote cast by increase # of votes
        number_of_votes = number_of_votes+1
        #Find candidate names by If column #2 of csv_path not equal candidate_list then  add the new name to the candidate_list
        if row[2] not in candidate_list:
            [candidate_list.append(row[2])]
        # Find The total number of votes each candidate won by create dictionary
        #if row[2] = candidate_list:

                    



#A complete list of candidates who received votes


 
    
        
    
    
    #for row in data 
    
    #candidates_and_votes.append((len(candidates_and_votes)))
    #print(candidates_and_votes.count("Khan"))

    




print("----------------")
print('Election Results')
print('Total votes = ' +str(number_of_votes-1))
print('----------------')
print(candidate_list)
#print("votes per candidates")






