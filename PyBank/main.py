import os # This will allow us to create file paths across operating systems
import csv # Module for reading CSV files
#ruta = "C:\Users\jlozan02\OneDrive - Kearney\Documents\Data-Analyst\Projects\python-challenge\python-challenge\PyBank\Resources"
# Specify the file to write to
output_path = os.path.join('Resources','budget_data.csv')
Report_path = os.path.join('Analysis','myreport.txt')
myreport = open(Report_path, 'w')
with open(output_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # Read each row of data after the header
    t = 0
    tm = 0
    pl = 0
    pre_rev = 0
    total_ch = 0
    inc = ['',0]
    dec = ['',0]
    for row in csvreader:
        rev = int(row[1])
        if pre_rev == 0:
            pre_rev = rev
        change = rev - pre_rev
        total_ch += change # total_ch = total_ch + change
        pre_rev = rev
        # greatest increase
        if change > inc[1]:
            inc[1] = change
            inc[0] = row[0]
         # greatest decrease
        if change < dec[1]:
            dec[1] = change
            dec[0] = row[0]
        t = t + rev
        tm = tm + 1
output = f'''
Financial Analysis
----------------------------
Total Months: {tm}
Total: ${t:,}
Average Change: ${total_ch/(tm-1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''
print(output)
myreport.write(output)