import sys

for line in sys.stdin:
    print(line.replace("\t", " "), end="")

# python 11.py < popular-names.txt | less

# sed -e 's/\t/ /g' popular-names.txt

# 読む、置き換え、書き込むでもいける

# sedコマンド
# -eで操作記述
# sコマンドは正規表現だと

# tr
# １文字を１文字

# expand
# タブをスペースに