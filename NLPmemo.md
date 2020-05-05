# 言語処理100本ノック2020を学ぶ際のメモ

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