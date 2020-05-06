str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = str.split()
discri = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = {}

for i in range(len(words)):
    word = words[i]
    word.rstrip(",.")
    if i+1 in discri:
        ans[word[0]] = i+1
    else:
        ans[word[:2]] = i+1

print(ans)