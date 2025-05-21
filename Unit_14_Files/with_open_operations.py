
with open("file.txt", "r+") as f:
    num_1 = int(f.readline())
    num_2 = int(f.readline())
    product = num_1 * num_2

    f.write("\n")
    f.write(str(product))


