# coding: utf-8
import mecabfunc
from collections import Counter

# 形態素解析
mecabfunc.parse_txt()

# *1
# オブジェクト作成、ここに表層形を入れていく
word_counter = Counter()

lines = mecabfunc.fix_mecab()
for line in lines:
    # *2
    word_counter.update([morpheme['surface'] for morpheme in line])

# 出現頻度順のリストを取得
commonwords_list = word_counter.most_common()

# print(commonwords_list)

# 先頭20個の要素表示
for i, commonword_list in enumerate(commonwords_list):
    if i == 20:
        break
    print(commonword_list, end=',')
print('')