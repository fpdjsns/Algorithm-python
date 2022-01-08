# problem : https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145
# algorithm : DP
# time complexity : O(N)

from math import inf

C = 0
J = 1

t = int(input())
for tc in range(1, t + 1):
    inputs = [s for s in input().split(" ")]
    X = int(inputs[0])  # CJ
    Y = int(inputs[1])  # JC
    S = inputs[2]
    N = len(S)

    # dp[0][i] = S[i]가 'C' 일 때, S[:i] 까지 최소 지불금액
    # dp[1][i] = S[i]가 'J' 일 때, S[:i] 까지 최소 지불금액
    dp = [[inf for i in range(N)] for j in range(2)]
    if S[0] != 'C':
        dp[J][0] = 0
    if S[0] != 'J':
        dp[C][0] = 0
    for i in range(1, N):
        now = S[i]
        if now != 'C': 
            dp[J][i] = min(dp[J][i - 1], dp[C][i - 1] + X)  # JJ, CJ
        if now != 'J':
            dp[C][i] = min(dp[C][i - 1], dp[J][i - 1] + Y)  # CC, JC

    print("Case #{}: {}".format(tc, min(dp[C][N - 1], dp[J][N - 1])))
