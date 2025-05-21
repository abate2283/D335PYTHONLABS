import os
import datetime
# myFile = open("../log/1970/8/25/log.txt", "w+")
# print(myFile.write("This is a new file"))
# myFile.close()

current_date = datetime.date(1970, 8, 25)
num_days = 30
for i in range(num_days):
    day = str(current_date.day)
    month = str(current_date.month)
    year = str(current_date.year)
    file_path = os.path.join("log", year, month, day, "log.txt")
    f = open(file_path, "r+")
    print(f"{file_path}:{f.read}")
    curr_day = curr_day + datetime.timedelta(days=1)


#
# import os
# import datetime
#
# curr_day = datetime.date(1997, 8, 29)
#
# num_days = 30
# for i in range(num_days):
#     year = str(curr_day.year)
#     month = str(curr_day.month)
#     day = str(curr_day.day)
#
#     # Build path string using current OS path separator
#     file_path = os.path.join('logs', year, month, day, 'log.txt')
#
#     f = open(file_path, 'r')
#
#     print(f'{file_path}: {f.read()}')
#     f.close()
#
#     curr_day = curr_day + datetime.timedelta(days=1)