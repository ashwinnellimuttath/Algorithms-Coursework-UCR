


C = 8

profit = [4,4,7,1]
weight = [5,2,3,1]

dp = [0] * (C + 1)

# for i in range(len(profit)):
#     dp[i][0] = 0
for c in range(C+1):
    if weight[0] <= c:
        dp[c] = profit[0]

for i in range(1,len(profit)):
    currentRow = [0] * (C + 1)
    for c in range(len(currentRow)):
        skip = dp[c]
        p = 0
        if c - weight[i] >= 0:
            p = profit[i] + dp[c-weight[i]]
        currentRow[c] = max(p,skip)
    dp = currentRow

print (dp[C])

