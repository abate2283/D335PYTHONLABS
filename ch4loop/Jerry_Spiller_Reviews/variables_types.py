# int # this is an integer
# float #
# bool #
# str #
# list #
# dict # {key: value} use the key[index] as a list to get the values
# set # {} has no order, all unique
# tuple #
# range #
# file # open() f.read() f.write()
myList = [2, "boy", 44]
word = {"a": 1, "b": 2}
d = {1:"int", 2.2 : "float", True:"bool",
     "value" : "str", "list":myList, "dic" : word,
     # "set", "tuple", "tuple",
     # "range", "file"}
     }
# print(d[1])
# for k,v in d.items():
#     print(k,":",v)

# for key in d:
#     print(key)
for value in d:
    print(d[value])
