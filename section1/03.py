str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = str.split() # 空白文字で分ける
ans = []
for word in words:
    ans.append(len(word.rstrip(",."))) # 右端から,または.をできるだけ削る

print(ans)

# generator式