# Add your encryption methods here
def encode(s, key):
    acc = ""
    for i in range(len(s)):
        temp = ord(s[i]) + key
        newChar = chr(temp)
        acc += newChar
    return acc


def encode_better(s, key):
    acc = ""
    for i in range(len(s)):
        temp = ord(s[i])
        k = ord(key[i % len(key)]) - 97
        temp += k
        newChr = chr(temp)
        acc += newChr
    return acc
