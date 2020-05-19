lines = open("popular-names.txt").readlines()
lines.sort(key = lambda line: float(line.split("\t")[2]), reverse=True)

for line in lines:
    print(line, end="")

# sort -k3 -nr popular-names.txt