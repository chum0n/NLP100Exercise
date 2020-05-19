with open("col1.txt") as f1, open("col2.txt") as f2, open("merge.txt", "w") as outf:
    for col1, col2 in zip(f1, f2):
        outf.write(col1.rstrip() + "\t" + col2.rstrip() + "\n")