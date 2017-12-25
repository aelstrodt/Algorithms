# Dynamic Programming

def longest_sub_sequence(s1, s2):
    l_s1 = len(s1)
    l_s2 = len(s2)
    dp = [[0 for _ in range(l_s1 + 1)] for _ in range(l_s2 + 1)]
    # if either one is empty -> longest sub_sequence = 0
    # already set
    for i in range(1, l_s1 + 1):
        for j in range(1, l_s2 + 1):
            if s2[j - 1] == s1[i - 1]:
                dp[j][i] = 1 + dp[j - 1][i - 1]
            else:
                # if we can't match, take max of prev cases
                dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
    return dp[-1][-1]

def knapsack(w, v, Wt):
    l_items = len(v)
    dp = [[0 for _ in range(Wt + 1)] for _ in range(l_items + 1)]
    # 0 size or 0 items -> 0 max value
    for i in range(1, l_items + 1):
        for j in range(1, Wt + 1):
            # if item doesn't fit, take value found without it
            if w[i - 1] > j:
                dp[i][j] = dp[i-1][j]
            # else take max of including vs not including item
            else:
                dp[i][j] = max(dp[i-1][j], v[i - 1] + dp[i - 1][j - w[i - 1]])
    # which items are included?
    return dp[-1][-1]
