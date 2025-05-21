import csv

with open("myCsv.csv", "r+") as c:
    result = csv.reader(c)
    for index in result:
        print(index)
