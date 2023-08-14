


C = 8

profit = [4,4,7,1]
weight = [5,2,3,1]

dp = [[-1] * (C + 1) for _ in profit]


def dfs(i,capacity, dp):
    if i == len(profit):
        return 0
    if dp[i][capacity] != -1:
        return dp[i][capacity]

    dp[i][capacity] = dfs(i+1, capacity,dp)

    newCapacity = capacity - weight[i]
    if newCapacity >= 0:
        p = profit[i] + dfs(i+1, newCapacity,dp)
        dp[i][capacity] = max(dp[i][capacity],p)

    print(capacity,i, "capacity")
    # print(C, "C")
    return dp[i][capacity]

print(dfs(0,C,dp))