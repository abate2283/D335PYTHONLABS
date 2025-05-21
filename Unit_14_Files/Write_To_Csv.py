import csv

row1 = ['100', '50', '29']
row2 = ['76', '32', '330']

with open("rowWrite.csv", "w") as writer_csv:
    myWriter = csv.writer(writer_csv)
    myWriter.writerow(row1)
    myWriter.writerow(row2)