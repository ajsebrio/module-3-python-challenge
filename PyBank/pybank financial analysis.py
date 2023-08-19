#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

pybank_csv = os.path.join('.', 'Resources', 'budget_data.csv')

output_file = os.path.join('.', 'financial_analysis.txt')

total_months = 0
total_amount = 0

net_change_list = []
month_of_changes = []

greatest_increase = ["", 0]
greatest_decrease = ["" , 100000000000000000000000]

with open(pybank_csv) as budget_data:
    
    reader = csv.reader(budget_data, delimiter=',')
    csv_header = next(reader)
    
    
    first_row = next(reader)
    total_amount += int(first_row[1])
    previous_net = int(first_row[1])
    total_months += 1
    
    for rows in reader:
        
        # calculate total months
        total_months += 1
        
        # calculate total
        total_amount += int(rows[1])
        
        # calculate the changes in “Profit/Losses” over the entire period, and then the average of those changes
        net_change = int(rows[1]) - previous_net
        previous_net = int(rows[1])
        net_change_list.append(net_change)
        net_monthly_average = round((sum(net_change_list) / len(net_change_list)), 2)
       
    
        # The greatest increase in profits (date and amount) over the entire period
        if(net_change > greatest_increase[1]):
                greatest_increase[0] = rows[0]
                greatest_increase[1] = net_change
        
        
        # The greatest decrease in profits (date and amount) over the entire period
        if(net_change < greatest_decrease[1]):
                greatest_decrease[0] = rows[0]
                greatest_decrease[1] = net_change
  
        
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_amount}\n"
    f"Average Change: ${net_monthly_average}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
)

print(output)

with open(output_file, 'w') as txt_file:
    txt_file.write(output)
              


# In[ ]:




