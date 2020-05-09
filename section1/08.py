def cipher(str):
    result = ""
    for char in str:
        if char.islower():
            result += chr(219- ord(char))
        else:
            result += char
    return result

str = input("Please enter a string >>>")

encrypted = cipher(str)
print(encrypted)

decrypted = cipher(encrypted)
print(decrypted)