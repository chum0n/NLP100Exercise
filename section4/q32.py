# coding: utf-8
import mecabfunc

# 形態素解析
mecabfunc.parse_txt()

# 先ほどの書き方
# # 1文ずつ辞書のリストを取得し動詞を抽出
# verbs_set = set() # 動詞を入れていく
# verbs_list = [] # 出現順を確認するためのリスト

# # linesは1文の各形態素を辞書化したリスト
# lines = mecabfunc.fix_mecab()
# for line in lines:
#     for morpheme in line:
#         if morpheme['pos'] == '動詞':
#             verbs_set.add(morpheme['base'])
#             verbs_list.append(morpheme['base'])

# リスト内包表記
verbs_list = []
for line in mecabfunc.fix_mecab():
    # *1
    verbs_list.extend(
        [morpheme['base'] for morpheme in line if morpheme['pos'] == '動詞']
    )
# リストを丸ごとsetに
verbs_set = set(verbs_list)


# # verbs_listを使って出現順にソートして表示
# print(sorted(verbs_set, key=verbs_list.index))

# 先頭10個の要素表示
for i, verb_set in enumerate(sorted(verbs_set, key=verbs_list.index)):
    if i == 10:
        break
    print(verb_set, end=',')
print('')

# 先頭10個の要素表示
for i, verb_list in enumerate(verbs_list):
    if i == 10:
        break
    print(verb_list, end=',')
print('')
