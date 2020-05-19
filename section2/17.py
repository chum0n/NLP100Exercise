with open("popular-names.txt") as data:
    ans_set = set()

    for line in data:
        cols = line.split("\t")
        ans_set.add(cols[0])

for ans in ans_set:
    print(ans)