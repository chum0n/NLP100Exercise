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
    for morpheme in line:
        # *1
        if morpheme['surface'] == '猫':
            word_counter.update(other_mor['base'] for other_mor in line if other_mor['surface'] != '猫')
            break

# 出現頻度が高い10語のリストを取得 *1
commonwords_list = word_counter.most_common(10)

print(commonwords_list)

# 単語と出現数のリストに分解 *2
zipped_cwlist = list(zip(*commonwords_list))
words = zipped_cwlist[0]
counts = zipped_cwlist[1]

# グラフを書く *3
# 日本語表示させるため *3
font_path = './07Yasashisa/07やさしさゴシック.ttf'
font_prop = FontProperties(fname=font_path)

plt.bar(
    range(0, 10), # x軸
    counts, #y軸
    align='center' # 真ん中に表示
)

# x軸に関する指定
plt.xticks(
    range(0, 10), # 値
    words, # それに対応するラベル
    fontproperties=font_prop # 日本語のため
)

# タイトルとラベルとグリッド *5
plt.title("The 10 most frequently co-occurring words")
plt.xlabel("word")
plt.ylabel("frequency")
plt.grid(axis='y')

# # 表示(グラフ保存の時は見れない)
# plt.show()

# グラフの保存 *6
plt.savefig("graph37.png")