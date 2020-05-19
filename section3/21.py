import gzip
import json
import re


def extract_UK():

    with gzip.open('jawiki-country.json.gz', 'rt') as data:
        for line in data:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    raise ValueError('イギリスの記事が見つからない')


# 正規表現のコンパイル
pattern = re.compile(r'''
    ^   # 行頭
    (   # キャプチャ対象のグループ開始
    .*  # 任意の文字0文字以上
    \[\[Category:
    .*  # 任意の文字0文字以上
    \]\]
    .*  # 任意の文字0文字以上
    )   # グループ終了
    $   # 行末
    ''', re.MULTILINE + re.VERBOSE)

# 抽出
result = pattern.findall(extract_UK())

# 結果表示
for line in result:
    print(line)