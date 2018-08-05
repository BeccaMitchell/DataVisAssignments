import os
import csv

file_path = os.path.join('Resources','budget_data.csv')

months = []
revenue = []
total_revenue = 0
profit_change = []
profit_months=[]

with open(file_path) as file:
    data = csv.reader(file,delimiter=',')
    next(data)
    
    for row in data:
        #create list of months
        months.append(row[0])
        
        #create list of revenue & calculate total net profits
        x = int(row[1])
        revenue.append(int(x))
        total_revenue += x
        
        #create list of profit changes and list of related months
        profit_change = [(revenue[r]-revenue[r-1]) for r in range(1, len(revenue))]
        profit_months = [months[m] for m in range(1, len(months))]
    
    #calculate average change in revenue between consecutive months
    average_change = round(sum(profit_change)/len(profit_change), 2)
    
    #find indices of max/min in list
    find_max_index = profit_change.index(max(profit_change))
    find_min_index = profit_change.index(min(profit_change))
        
print("Total months: "+ str(len(months)))
print("Total: $"+str(total_revenue))
print("Average change: $"+str(average_change))
print("Greatest increase in profits: "+str(profit_months[find_max_index])+" $"+str(profit_change[find_max_index]))
print("Greatest decrease in profits: "+str(profit_months[find_min_index])+" $"+str(profit_change[find_min_index]))

output_file = os.path.join("Resources", "PyBank_output.csv")

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Question', 'Answer'])
    csvwriter.writerow(['Total months: ', len(months)])
    csvwriter.writerow(['Total: $ ', total_revenue])
    csvwriter.writerow(['Greatest increase in profits: ',profit_months[find_max_index], profit_change[find_max_index]])
    csvwriter.writerow(['Greatest decrease in profits: ',profit_months[find_min_index], profit_change[find_min_index]])
