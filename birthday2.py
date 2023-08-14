m = 10
prices = [4, 3, 10, 8, 5, 6, 3, 12, 4]

# m = int(input())
# prices = list(map(int, input().split()))

dp = [0] * (m + 1)
for i in range(1, m+1):
    for j in range(1,10):
        # if i - prices[j-1] < 0 : break
        if prices[j-1] <= i:
            first = str(j) + str(dp[i-prices[j-1]])
            if dp[i-prices[j-1]] == 0:

                first = str(j)
            dp[i] = max(dp[i],int(first))
            # dp[i] = max(dp[i], int(str(j) + str(dp[i-prices[j-1]])))

print(dp)