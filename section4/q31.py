# coding: utf-8
import mecabfunc

# 形態素解析
mecabfunc.parse_txt()

# 1文ずつ辞書のリストを取得し動詞を抽出
verbs_set = set() # 動詞を入れていく *1
verbs_list = [] # 出現順を確認するためのリスト

# linesは1文の各形態素を辞書化したリスト
lines = mecabfunc.fix_mecab()
# *2
for line in lines:
    for morpheme in line:
        if morpheme['pos'] == '動詞':
            verbs_set.add(morpheme['surface'])
            verbs_list.append(morpheme['surface'])

# # verbs_listを使って出現順にソートして表示 *3
# print(sorted(verbs_set, key=verbs_list.index))

# 先頭10個の要素表示
for i, verb in enumerate(sorted(verbs_set, key=verbs_list.index)):
    if i == 10:
        break
    print(verb, end=',')
print('')

# 先頭10個の要素表示
for i, verb_test in enumerate(verbs_list):
    if i == 10:
        break
    print(verb_test, end=',')
print('')
