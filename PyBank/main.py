import os
import csv

# Path to collect data from folder
budget_dataCSV = os.path.join('budget_data.csv')


# Calculate the following
# The total number of months included in the dataset (done)
# The total net amount of "Profit/Losses" over the entire period (done)
# The average change in "Profit/Losses" between months over the entire period (done)
# The greatest increase in profits (date and amount) over the entire period (done)
# The greatest decrease in losses (date and amount) over the entire period (done)

# Opening csv file as read and calling it csvfile
with open(budget_dataCSV, 'r') as csvfile:
    
    # Identifying the csv file delimiter with commas which will be able to tell every column
    csvreader = csv.reader(csvfile,delimiter=',')

    # Removing header as part of data from CSV file
    header = next(csvreader)

    # Identifying data as a list 
    data = list(csvreader)

    # Counting the length of the list of data
    row_count = len(data)
    
    # Print header
    print("Financial Analysis")
    print("----------------------------")

    # Printing the total list of dates
    print("Total Months: "+ str(row_count))

    # Set total to 0
    total_revenue = 0

    # Set revenue to be a list
    revenue = []

    # For loop through rows of data, indicating [1] is the Revenue column in csv. Make sure to make a int so it can stay a number. 
    # .append is adding an item to existing list. This is why we made revenue = [] above

    for row in data:
        total_revenue += int(row[1])
        revenue.append(int(row[1]))

    print("Total Revenue: "+ '${}'.format(total_revenue))

# calculate difference by making taking revenue after subtract revenue before looping through the rows of revenue.
# doing minus 1 at the end because the last row will not be able to run this function
difference = [revenue[i+1]-revenue[i] for i in range(len(revenue)-1)]

# Set Sum of difference and Number of Items in difference as 0 to start
sum_difference = 0
num_items_difference = 0

# Set Max & Min of the difference as variable
max_difference = max(difference)
min_difference = min(difference)

# for loop through the items in the differences list and add up the items
# for loop through the items in the differences list and add up number of items
# len can be used as well len(difference) instead of defining num_items_difference and looping
for item in difference:
    sum_difference += item
    num_items_difference +=1

avg_difference = round(sum_difference/num_items_difference,2)

print("Average Change: " + '${}'.format(str(avg_difference)))
print("Greatest Increase in Profits: " + '${}'.format(str(max_difference)))
print("Greatest Decrease in Profits: " + '${}'.format(str(min_difference)))


# Create path to create txt file. Write out the output in file.write
file = open('budget_output.txt','w')

file.write("Financial Analysis: Total Months- 41, Total Revenue- $18971412, Average Change- $-6758.98, Greatest Increase in Profits- $1837235, Greatest Decrease in Profits: $-1779747")

file.close()



