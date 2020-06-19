# coding: utf-8
import CaboCha

def parse_txt():

    with open('ai/ai.ja.txt') as data_file, \
            open('ai.ja.txt.parsed', mode='w') as out_file:

        cabocha = CaboCha.Parser()
        for line in data_file:
            out_file.write(
                cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
            )


class Morph:

    def __init__(self, surface, base, pos, pos1):
        '''初期化'''
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        # オブジェクトの文字列表現
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
            .format(self.surface, self.base, self.pos, self.pos1)

# 係り受け解析結果のジェネレータ
def fix_cabocha():

    with open('ai.ja.txt.parsed') as file_parsed:

        morphs = []
        for line in file_parsed:

            # 1文の終了判定
            if line == 'EOS\n':
                yield morphs
                morphs = []

            else:
                # 先頭が*の行は係り受け解析結果なのでスキップ
                if line[0] == '*':
                    continue

                # 表層形はtab区切り、それ以外は','区切りでバラす
                cols = line.split('\t')
                res_cols = cols[1].split(',')

                # Morph作成、リストに追加
                morphs.append(Morph(
                    cols[0],        # surface
                    res_cols[6],    # base
                    res_cols[0],    # pos
                    res_cols[1]     # pos1
                ))

        raise StopIteration