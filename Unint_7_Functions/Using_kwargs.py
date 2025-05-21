# *args or **kwargs

def print_stats(name, **info):
    print(name, "is")
    for key, values in info.items():
        print(f"{key} : {values}")


print_stats("Alfred A Bate", age=54, city="Broken Arrow")
