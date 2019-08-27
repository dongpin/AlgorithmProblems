# 205. Isomorphic Strings

from collections import defaultdict


def is_isomorphic(s, t):
    if not s and not t:
        return True
    if not s or not t or len(s) != len(t):
        return False

    chars = defaultdict()
    exist = set()
    for i in range(len(s)):
        if s[i] not in chars:
            if t[i] in exist:
                return False
            chars[s[i]] = t[i]
            exist.add(t[i])
        elif chars[s[i]] != t[i]:
            return False
    return True
