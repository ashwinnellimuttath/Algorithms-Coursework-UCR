n, k = map(int, input().split())
cost = [0] * k
for i in range(k):
    cost[i] = int(input())
s = input().strip()
dp = [[0] * n for _ in range(n)]
for l in range(2, n+1):
    for i in range(n-l+1):
        j = i + l - 1
        print(i,j)
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1]
        else:
            # dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + cost[min(ord(s[i])-ord('a'), ord(s[j])-ord('a'))]
            dp[i][j] = min(dp[i+1][j] + cost[ord(s[i])-ord('a')], dp[i][j-1] + cost[ord(s[j])-ord('a')])
print(dp)




# n, k = map(int, input().split())
# p = [0] * 26
# for i in range(k):
#     print(k,input())
#     p[ord(input()) - ord('a')] = int(input())
# s = input().strip()

# dp = [[0] * n for _ in range(n)]
# for L in range(2, n+1):
#     for i in range(n-L+1):
#         j = i + L - 1
#         if s[i] == s[j]:
#             dp[i][j] = dp[i+1][j-1]
#         else:
#             dp[i][j] = min(p[ord(s[i]) - ord('a')] + dp[i+1][j], p[ord(s[j]) - ord('a')] + dp[i][j-1])

# print(dp[0][n-1])
