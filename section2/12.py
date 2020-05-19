import sys

with open("col1.txt", "w") as f1, open("col2.txt", "w") as f2: # fileなかったら勝手に作られる
    for line in sys.stdin:
        cols = line.rstrip("\n").split("\t") # cols[-1]に改行文字が含まれてしまうのを防ぐためにrstrip
        print(cols[0], file=f1)
        print(cols[1], file=f2)