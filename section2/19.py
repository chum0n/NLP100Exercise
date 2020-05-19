from collections import Counter
import sys

col1_set = Counter(line.split("\t")[0] for line in sys.stdin)
for word, num in col1_set.most_common():
    print(num, word)

# cut -f1 popular-names.txt | sort | uniq -c | sort -nr