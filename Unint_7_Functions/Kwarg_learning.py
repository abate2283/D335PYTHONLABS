info = {"Peters Elementary School": "5th grade", "Anderson": "2nd grade", "CAP Disney": "Early 2 year olds"}
student = ["Angel", "Zion", "Mercy", "Alfred"]


def biographic_infor(student, **info):
    print(student, "details")
    for i in student:
        print(student[i])
    for key, value in info.items():
        print(f"{info[key]} : {info[value]}")


biographic_infor("Angel Bate", school="Peters Elementary School", grade="4th grade")
biographic_infor(student, info)
