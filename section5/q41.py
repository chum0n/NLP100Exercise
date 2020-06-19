# coding: utf-8
import cabochafunc
import re

class Chunk:
    '''
    文節クラス
    形態素（Morphオブジェクト）のリスト（morphs）、係り先文節インデックス番号（dst）、
    係り元文節インデックス番号のリスト（srcs）をメンバー変数に持つ
    '''

    def __init__(self):
        '''初期化'''
        self.morphs = []
        self.srcs = []
        self.dst = -1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)

# 係り受け解析
cabochafunc.parse_txt()

# 1文ずつリスト作成
for i, chunks in enumerate(cabochafunc.fix_cabocha(), 1):

    # 8文目を表示
    if i == 8:
        for j, chunk in enumerate(chunks):
            print('[{}]{}'.format(j, chunk))
        break