def ngram(n, str):
    words = []
    for i in range(len(str)-n+1):
        words.append(str[i:i+n])
    return words

str = "I am an NLPer"
words = str.split()
print(ngram(2, words)) # 単語なので分解したものを
print(ngram(2, str)) # 文字なのでstrそのまま

