import csv

## creating employee-meetings.csv file.
data_dict = [{"Employee Id":"001",'Employee Name':'Alex','In-time':'9:20','Out-time':'18:30',"Break-time":'13:30 - 14:30',"Meeting-time":"15:00 - 15:40"},
{"Employee Id":"002","Employee Name":"John","In-time":"9:15","Out-time":"18:20","Break-time":"13:30 - 14:30","Meeting-time":"15:10 - 15:40"},
{"Employee Id":"003","Employee Name":"Musk","In-time":"9:25","Out-time":"18:30","Break-time":"13:15 - 14:00","Meeting-time":"15:00 - 15:45"}]

file_name = 'employee-meetings.csv'

with open(file_name,'w') as file:
    column_names = ['Employee Id','Employee Name', 'In-time','Out-time','Break-time','Meeting-time']
    writer = csv.DictWriter(file,fieldnames=column_names)
    writer.writeheader()
    writer.writerows(data_dict)
    
## Extracting the Data from employee-meetings.csv file.

row_data = []
with open("employee-meetings.csv",'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)

    for row in csvreader:
        row_data.append(row)

print(header)
print(row_data[1])


## updating data in csv file 


for row in row_data:
    if(row["Employee Id"] == "002"):
        row["Employee Name"] == "Dravid" 

print(row_data)

