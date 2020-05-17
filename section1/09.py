import random

def rampro(str):
    # 無理だった
    # result = ""
    # words = str.split()
    # for word in words:
    #     if len(word) <= 4:
    #         result += word
    #     else:
    #         med_str = random.shuffle(word[1:-1])
    #         result += word[0] + med_str + word[-1]

    # return result
    result = []
    words = str.split()
    for word in words:
        if len(word) <= 4:
            result.append(word)
        else:
            med_str = list(word[1:-1])
            random.shuffle(med_str)
            result.append(word[0] + "".join(med_str) + word[-1]) # 間に文字列なし

    return " ".join(result) # 間に空白入れる

# 対象文字列の入力
target = input("Please enter a string >>>")

ans = rampro(target)
print("result:" + ans)