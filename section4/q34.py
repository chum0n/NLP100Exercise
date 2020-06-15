# coding: utf-8
import mecabfunc

# 形態素解析
mecabfunc.parse_txt()

# 出現順で格納されるリスト
multinouns_list = []

lines = mecabfunc.fix_mecab()
for line in lines:
    # 見つけた名詞を追加していくリスト
    nouns = []
    for morpheme in line:

        # 名詞ならnounsに追加
        if morpheme['pos'] == '名詞':
            nouns.append(morpheme['surface'])

        # 名詞以外なら、それまでの連続する名詞をmultinouns_listに追加
        else:
            if len(nouns) > 1: # 名詞が二つ以上続いている語であれば
                # *1
                multinouns_list.append(''.join(nouns))
            nouns = []

# リストを丸ごとsetに
multinouns_set = set(multinouns_list)

# # multinouns_listを使って出現順にソートして表示
# print(sorted(multinouns_set, key=multinouns_list.index))

# 先頭40個の要素表示
for i, multinoun_set in enumerate(sorted(multinouns_set, key=multinouns_list.index)):
    if i == 40:
        break
    print(multinoun_set, end=',')
print('')

# 先頭40個の要素表示
for i, multinoun_list in enumerate(multinouns_list):
    if i == 40:
        break
    print(multinoun_list, end=',')
print('')