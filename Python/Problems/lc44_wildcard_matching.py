# 44. Wildcard Matching

def is_match(s, p):
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
                d[p_index][s_index] = True
                s_index += 1
        # the current character in the pattern is '?'
        elif p[p_index-1] == '?':
            for s_index in range(1, len(s) + 1): 
                dp[p_idx][s_idx] = dp[p_index-1][s_index-1] 
        # the current character in the pattern is not '*' or '?'
        else:
            for s_index in range(1, len(s) + 1): 
                # Match is possible if there is a previous match
                # and current characters are the same
                dp[p_index][s_index] = \
                    dp[p_index-1][s_index-1] and p[p_index-1] == s[s_index-1]  
                                                               
        return dp[len(p)][len(s)]