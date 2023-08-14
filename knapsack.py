W, n = map(int, input().split())
weights = [0]
values = [0]
for i in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[0 for j in range(W+1)] for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, W+1):
        if weights[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])

print(dp[n][W])