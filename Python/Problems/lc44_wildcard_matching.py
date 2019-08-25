# 44. Wildcard Matching

def is_wildcard_match(s, p):

    def match(s, p):

        if (s, p) in memo:
            return memo[(s, p)]

        if s == p or p == '*':
            memo[(s, p)] = True
        elif p == '' or s == '':
            memo[(s, p)] = False
        elif p[0] == s[0] or p[0] == '?':
            memo[(s, p)] = match(s[1:], p[1:])
        elif p[0] == '*':
            memo[(s, p)] = match(s[1:], p) or match(s, p[1:])
        else:
            memo[(s, p)] = False
        return memo[(s, p)]

    def remove_duplicate_stars(p):
        if p == '':
            return p
        i = 0
        stack = []
        while i < len(p):
            if not (stack and stack[-1] == '*' and p[i] == '*'):
                stack.append(p[i])
            i += 1
        return ''.join(stack)

    p = remove_duplicate_stars(p)

    memo = {}
    return match(s, p)


'''
def is_wildcard_match(s, p):
    if p == s or p == '*':
        return True
    if not p and not s:
        return True

    dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]

    dp[0][0] = True

    for p_index in range(1, len(p)+1):
        if p[p_index-1] == '*':
            s_index = 1
            # d[p_idx - 1][s_idx - 1] is a string-pattern match
            # on the previous step, i.e. one character before.
            # Find the first idx in string with the previous math.
            while not dp[p_index-1][s_index-1] and s_index < len(s) + 1:
                s_index += 1
            # If (string) matches (pattern),
            # when (string) matches (pattern)* as well
            dp[p_index][s_index-1] = dp[p_index-1][s_index-1]
            # If (string) matches (pattern),
            # when (string)(whatever_characters) matches (pattern)* as well
            while s_index < len(s) + 1:
                dp[p_index][s_index] = True
                s_index += 1
        # the current character in the pattern is '?'
        elif p[p_index-1] == '?':
            for s_index in range(1, len(s) + 1):
                dp[p_index][s_index] = dp[p_index-1][s_index-1]
        # the current character in the pattern is not '*' or '?'
        else:
            for s_index in range(1, len(s) + 1):
                # Match is possible if there is a previous match
                # and current characters are the same
                dp[p_index][s_index] = \
                    dp[p_index-1][s_index-1] and p[p_index-1] == s[s_index-1]

        return dp[len(p)][len(s)]
'''
