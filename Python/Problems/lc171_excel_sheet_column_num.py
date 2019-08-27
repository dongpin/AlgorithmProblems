# 171. Excel Sheet Column Number


def title_to_num(s):
    num = 0
    for i in range(len(s)):
        num = num * 26 + (ord(s[i]) - ord('A') + 1)
    return num
