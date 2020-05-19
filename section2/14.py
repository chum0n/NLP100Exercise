n = int(input("N-->"))

with open("popular-names.txt") as data:
    for i, line in enumerate(data):
        if i >= n:
            break
        print(line.rstrip())