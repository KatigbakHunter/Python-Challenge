#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv

budget_csv = r"/Users/katigbakv/Desktop/module-3-re/PyBank/Resources/budget_data.csv"


total_net = 0
total_months = 0 
net_change_list = []
month_of_changes = []


greatest_increase = {"amount": float('-inf'), "month": ""}
greatest_decrease = {"amount": float('inf'), "month": ""}

with open(budget_csv, mode='r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)


    first_row = next(csvreader)
    total_net += int(first_row[1])
    previous_net = int(first_row[1])


    for row in csvreader:
        total_months += 1
        total_net += int(row[1])
        
        net_change = int(row[1]) - previous_net
        net_change_list.append(net_change)

        
        month_of_changes.append(row[0])
        previous_net = int(row[1])

        
        if net_change > greatest_increase["amount"]:
            greatest_increase["amount"] = net_change
            greatest_increase["month"] = row[0]

       
        if net_change < greatest_decrease["amount"]:
            greatest_decrease["amount"] = net_change
            greatest_decrease["month"] = row[0]


net_monthly_average = sum(net_change_list) / len(net_change_list)

print(f"Financial Analysis")
print(f"-------------------")
print(f"Total Net: ${total_net}")
print(f"Total Months: {total_months}")
print(f"Net Monthly Average: {net_monthly_average:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})")


output_file = r"/Users/katigbakv/Desktop/module-3-re/output/financial_analysis.txt"


with open(output_file, mode='w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-------------------\n")
    txt_file.write(f"Total Net: ${total_net}\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Net Monthly Average: {net_monthly_average:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})\n")


# In[ ]:




