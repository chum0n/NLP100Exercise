def ngram(n, str):
    words = []
    for i in range(len(str)-n+1):
        words.append(str[i:i+n])
    return words

X = set(ngram(2, "paraparaparadise"))
Y = set(ngram(2, "paragraph"))

print(X | Y)
print(X & Y)
print(X - Y)
print(Y - X)
print("se" in X)
print("se" in Y)