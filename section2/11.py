import sys

for line in sys.stdin:
    print(line.replace("\t", " "), end="")

# python 11.py < popular-names.txt | less

# sed -e 's/\t/ /g' popular-names.txt