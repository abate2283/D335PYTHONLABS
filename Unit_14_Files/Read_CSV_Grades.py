import csv

# with open("grades.csv", "r") as c:
#     csvReader = c.readline()
#     print(csvReader, end="")
#     for i in range(0, len(csvReader), 2):
#         report = {}
#         report.update({csvReader[i]:csvReader[i]})
#     for k,v in report.items():
#         print(f"Reports {k}:{v}")

with open("grades.csv", "r") as cfile:
    fileRead = cfile.readline()
    word = fileRead.split()

for index, w in enumerate(word):
    print(index, w)




