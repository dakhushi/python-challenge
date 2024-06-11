#Modules
import os
import csv

#Path to collect the data from the Resources folder
budget_data_csv = os.path.join("Resources","budget_data.csv")

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:
    csvreader =csv.reader(csvfile)
    header = next(csvreader)
       
    # Counters/variables to stroe the values
    total_Months = 0
    total_revenue = 0
    previous_revenue = None
    
    month_change_list = []
    revenue_change_list= []

    greatest_increase = ("", float('-inf'))
    greatest_decrease = ("", float('inf'))

    # Loop through all the rows in csv file
    for row in csvreader:
        
        #Count total number of months
        total_Months +=1

        #total revenue over entire period
        current_revenue = int(row[1])
        total_revenue += current_revenue

        #Calculate the average change in revenue between months over the entire period
        if previous_revenue is not None:
            revenue_change = current_revenue - previous_revenue
            revenue_change_list.append(revenue_change)

            #The greatest increase in profits (date and amount) over the entire period
            if revenue_change > greatest_increase[1]: 
                greatest_increase = (row[0], revenue_change)

            #The greatest decrease in losses (date and amount) over the entire period
            if revenue_change < greatest_decrease[1]:
                greatest_decrease = (row[0], revenue_change)

        #update previous revenue to current revenue for next iteration
        previous_revenue = current_revenue

    #calculate the average revenue change
    if revenue_change_list:
        average_change = sum (revenue_change_list)/len(revenue_change_list)
    else:
        verage_change =0

#set the output of the text file
output_path = os.path.join("analysis","Revenue_summary.txt")

#write analysis to text file, /n meanes write in new line

with open (output_path,'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write(".......................\n")
    textfile.write(f"Total Months: {total_Months}\n")
    textfile.write(f"Total Revenue: ${total_revenue:,}\n")
    textfile.write(f"Average Change: ${average_change:,.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,})\n")
