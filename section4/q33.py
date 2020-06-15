# coding: utf-8
import mecabfunc

# 形態素解析
mecabfunc.parse_txt()

# 出現順で格納されるリスト
abs_list = []

lines = mecabfunc.fix_mecab()
# *1
for line in lines:
    for i in range(1, len(line) - 1):
        if line[i]['surface'] == 'の' \
                and line[i - 1]['pos'] == '名詞' \
                and line[i + 1]['pos'] == '名詞':
            abs_list.append(line[i - 1]['surface'] + 'の' + line[i + 1]['surface'])
# リストを丸ごとsetに
abs_set = set(abs_list)

# # abs_listを使って出現順にソートして表示
# print(sorted(abs_set, key=abs_list.index))

# 先頭40個の要素表示
for i, ab_set in enumerate(sorted(abs_set, key=abs_list.index)):
    if i == 40:
        break
    print(ab_set, end=',')
print('')

# 先頭40個の要素表示
for i, ab_list in enumerate(abs_list):
    if i == 40:
        break
    print(ab_list, end=',')
print('')