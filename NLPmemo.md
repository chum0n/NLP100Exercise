# 言語処理100本ノック2020を学ぶ際のメモ

## サイト

[言語処理100本ノック](https://nlp100.github.io/ja/)

[言語処理100本ノックでPythonに入門](https://qiita.com/hi-asano/items/02d82cc1e89fc663b4e6)

[素人の言語処理100本ノック:まとめ](https://qiita.com/segavvy/items/fb50ba8097d59475f760)

[言語処理100本ノック2020年版が公開！どこが変わったの？](https://qiita.com/hi-asano/items/3c17943ce06f9999ec6f)

## 第１章

スライスを使うと部分文字列を簡単に取得できる
- word[i:j]でi番目以上j番目未満の要素を取得
- iまたはjを省略すると「端」という意味になる
- 負の添え字を使うと文字列の後ろからアクセスできる

word[i:j:k]でi番目以上j番目未満の要素をk個毎に取得できる

リストのメソッド
- リスト.append():リストに要素を追加する

文字列型のメソッド
- x.split(sep):文字列xをsepで区切ることでリストを作ります。
- sep.join(list): listの要素をsepで結合した文字列を作ります
- x.strip(chars):文字列の両端からcharsを削った文字列を返します
- x.rstrip(chars):文字列の右端からcharsを削った文字列を返します

split(), strip(), rstrip()の引数を省略したときは「あらゆる空白文字」という意味になります

Cでの
```
int i;
int squares[6] = {1, 4, 6, 16, 25, 36};
int total = 0;
for(i = 0; i < 6; i++) {
    total += squares[i];
}
```
はPythonでは
```
total = 0
for square in squares:
    total += square
```

Pythonのprint()関数は（デフォルトでは）自動で改行してくれます。
改行を防ぐときは次のようにオプション引数endを指定します。
```
for square in squares:
    print(square, end=' ')
```

len()はリストや文字列などの長さを返します。

range()は一般にfor文をn回まわしたいときに使います。

組み込み関数zip()を使えばもっと簡単に書けます。この関数は引数のイテラブルオブジェクトからi番目の要素を組にしてくれます。

enumerate()を使うとループ回数をくっつけてくれる。
```
ans = {}
for i, word in enumerate(words, start=1): # 普通に使うと0から始まるので、オプション引数start=1を指定している
    if i in where:
        key = word[0]
    else:
        key = word[:2]
    ans[key] = i
```

[n-gramについて](https://qiita.com/kazmaw/items/4df328cba6429ec210fb)




printfの%fで小数を表示するときは、小数第6位まで表示するという決まりになっている。
「%f」を「%.2f」に書き換えてみると、小数第2位まで（3.14）が表示されます。同様に、「%.1f」なら「3.1」、「%.0f」なら「3」となります。

chr(i)  
Unicode コードポイントが整数 i である文字を表す文字列を返します。chr(97) は文字列 'a' を、 chr(8364) は文字列 '€' を返します。 ord() の逆です。

ord()  
chr()の逆

ランダムな並び替えはrandom.shuffle()が使える

文字列メソッドjoin()を使うと、文字列のリストを一つの文字列に連結することができる。  
'間に挿入する文字列'.join([連結したい文字列のリスト])

## 第二章

[UNIX/Linux 環境でのコマンドライン操作に慣れる…前の基礎知識](https://qiita.com/eumesy/items/6b0eda9f604934092857)

with構文は、f = open('popular-names.txt')の実行と、ブロックを抜けるときのf.close()を勝手にやってくれる優れものです。

ファイルを一度に複数個使うときはwith open('test1') as f1, open('test2') as f2のようにカンマを使います。

標準入力を一行ずつ読みたいときはsys.stdinを使います。これもファイルオブジェクトです。この章の問題は全て上の方法でできるのですが、標準入力を使う方が何かと便利です。

PythonではCのi++は使えないので累算代入演算子+=を使いましょう。

pass文は何もしたくないけど文法上何かを書く必要があるときに使います。

str.replace(old, new)を使ってみましょう。このメソッドは文字列中の部分文字列oldをnewに置換して返します。タブ文字はCと同じように\tとします。

sedのsコマンド： s/検索パターン/置換文字列/g（すべて置換）  
sed 's/\t/ /g' hightemp.txt

次の問題ではファイル書き込みについて学びます。テキストファイルを書き込みモードで開くときはopen(filename, 'w')を使います。

バックスラッシュ\を使うことで改行しても文が継続していると見なされます。

CSV（comma-separated values）ファイルなど、固定長ではなく「,（カンマ）」やタブで区切られているテキストに対し、何番目のフィールドかを指定したい場合は「-f」オプションを使用します。

「cut」は、ファイルを読み込んで、それぞれの行から指定した部分だけを切り出すコマンドです。

複数のファイルを行単位で連結する「paste」コマンド