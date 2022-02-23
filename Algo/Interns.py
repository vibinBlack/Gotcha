import csv
import pandas as pd

n = int(input("Enter the method to be executed \n For using pandas Enter 4 \n 1 or 2 or 3 or 4 \t: "))

if n ==1:
    file = open("C:/Users/Vinay Muthangi/Gotcha/Algo/Interns.csv")

    csvreader = csv.reader(file)

    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    for i in rows:
        print(i)
    file.close()

elif n == 2:
    rows = []
    with open('C:/Users/Vinay Muthangi/Gotcha/Algo/Interns.csv','r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
        print(header)
        for i in rows:
            print(i)

elif n == 3:
    with open("C:/Users/Vinay Muthangi/Gotcha/Algo/Interns.csv") as file:
        content = file.readlines()
    header = content[:1]
    rows = content[1:]
    print(header)
    for i in rows:
        print(i)
elif n == 4:
    csvreader = pd.read_csv("C:/Users/Vinay Muthangi/Gotcha/Algo/Interns.csv")

    print(csvreader.head())
    col_names = list(csvreader.columns)
    print(col_names)

    print(csvreader.Name +"     "+ csvreader.College)

