str1 = "パトカー"
str2 = "タクシー"

for i in range(len(str1)):
    print(str1[i]+str2[i], end="")

# zip()使ったやり方
# for a, b in zip(str1, str2):
#     print(a+b, end='')
# どっちか要素切れたら終わる

# 文字列を作ってから最後にjoinという方法もある

# 末尾に改行入れるため
print("")