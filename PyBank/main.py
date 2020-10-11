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


#Calculate the net total amount of "Profit/Losses" over the entire period
#Calculate the average of the changes in "Profit/Losses" over the entire period
#months = 86
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
greatest_increase=max(profits_losses)
greatest_decrease=min(profits_losses)



print("    ")
print("Output")
print('Total number of months is ' + str(number_of_months-1))
print('Total amount of Profit/losses is ' + str(net_profit))
print('Average Profit/losses is ' +str(average_change))
print("The greatest increase is " + str(greatest_increase))
print("The greatest decrease is " + str(greatest_decrease))



# export file as a result

# Specify the file to write to
output_path = os.path.join("Analysis", "Analysis_file-PyBank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total months', 'Total amount', 'Average', 'Greatest increase', 'Greatest decrease'])

    # Write the second row
    csvwriter.writerow([str(number_of_months-1), str(net_profit), str(average_change),str(greatest_increase),str(greatest_decrease) ])



