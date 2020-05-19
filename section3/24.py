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
    (?:File|ファイル)   # 非キャプチャ、'File'か'ファイル'
    :
    (.+?)   # キャプチャ対象、任意の文字1文字以上、非貪欲
    \|
    ''', re.VERBOSE)

# 抽出
result = pattern.findall(extract_UK())

# 結果表示
for line in result:
    print(line)