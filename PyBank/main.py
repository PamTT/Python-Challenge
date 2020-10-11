#MainPy

import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#Calculate the total number of months included in the dataset
number_of_months=0
with open (csvpath,'r',) as csv_file:
    csv_reader_object = csv.reader(csv_file)
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        print("csv row: {0}".format(row))
        number_of_months = number_of_months+1
        csv_reader_object.line_num
print('total number of months ' + str(number_of_months-1))

#Calculate the net total amount of "Profit/Losses" over the entire period
months = 86
profits_losses=[]
with open (csvpath,'r',) as csv_file:
    for row in csv.reader(csv_file):
        profits_losses.append(row[1])
    profits_losses.remove("Profit/Losses")

    for i in range(0,len(profits_losses)):
         profits_losses[i] =int(profits_losses[i])   

print(profits_losses)

net_profit=sum(profits_losses)
average_change = net_profit/number_of_months

print('Total amount of Profit/losses is ' + str(net_profit))
print('Average Profit/losses is ' +str(average_change))


#Calculate the average of the changes in "Profit/Losses" over the entire period
#average_change = profits_losses/months
#print(average_change)


#Calcurate the greatest increase in profits (date and amount) over the entire period


#Calcurate the greatest decrease in losses (date and amount) over the entire period

# print

# export file as a result


