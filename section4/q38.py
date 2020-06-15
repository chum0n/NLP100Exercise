# coding: utf-8
import mecabfunc
from collections import Counter

# plt.show()で見たいときは以下の二文いらない
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 形態素解析
mecabfunc.parse_txt()

# オブジェクト作成、ここに表層形を入れていく
word_counter = Counter()

lines = mecabfunc.fix_mecab()
for line in lines:
    word_counter.update([morpheme['surface'] for morpheme in line])

# 出現頻度が高い順のリストを全て取得
commonwords_list = word_counter.most_common()

# 出現数のリストを取得
zipped_cwlist = list(zip(*commonwords_list))
counts = zipped_cwlist[1]

# グラフを書く
# 日本語表示させるため
font_path = './07Yasashisa/07やさしさゴシック.ttf'
font_prop = FontProperties(fname=font_path)

# ヒストグラム *1
plt.hist(
    counts, # ヒストグラムを作成するための生データの配列
    bins=25, # ビン (表示する棒) の数。階級数。デフォルトは10
    range=(1, 25) # ビンの最小値と最大値
)

# x軸の値の範囲の調整
plt.xlim(xmin=1, xmax=25)

# タイトルとラベルとグリッド
plt.title("Frequency of word occurrence")
plt.xlabel("frequency")
plt.ylabel("the number of types")
plt.grid(axis='y')

# # 表示(グラフ保存の時は見れない)
# plt.show()

# グラフの保存
plt.savefig("graph38.png")