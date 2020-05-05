str1 = "パトカー"
str2 = "タクシー"

for i in range(len(str1)):
    print(str1[i]+str2[i], end="")

# zip()使ったやり方
# for a, b in zip(str1, str2):
#     print(a+b, end='')

# 末尾に改行入れるため
print("")