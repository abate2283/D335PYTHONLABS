import csv

first_row = ["Daddy", "Mommy", "Angel", "Zion"]
second_row = ["Grandma Canada", "Grandma Buea Town", "Aunty Bene", "Aunty Ashu"]

# with open("our_file.csv", "w+") as fileCsv:
#     csvWriter = csv.writer(fileCsv)
#     csvWriter.writerow(first_row)
#     csvWriter.writerow(second_row)
#     csvWriter.writerows([first_row, second_row, first_row, second_row])


with open("our_file.csv", "r+") as f:
    myFiles = f.readlines()
    for lines in myFiles:
        # first_row = lines.rstrip().split()[0]
        first_row = lines.rstrip()[0]
        # second_row = lines.rstrip().split()[1]
        print(first_row)
        # print(second_row)
