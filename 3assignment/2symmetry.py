n, k = map(int, input().split())
p = list(map(int, input().split()))
s = input().strip()

# initialize dp array
dp = [[0] * n for _ in range(n)]

# base case: single-character substrings are already palindromes
for i in range(n):
    dp[i][i] = 0

# dynamic programming
for l in range(2, n+1):
    for i in range(n-l+1):
        j = i + l - 1
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1]
        else:
            dp[i][j] = min(dp[i+1][j] + p[ord(s[i])-ord('a')], dp[i][j-1] + p[ord(s[j])-ord('a')])

# output answer
print(dp[0][n-1])


# n, k = map(int, input().split())
# p = [0] * k
# for i in range(k):
#     p[i] = int(input())
# s = input()[:k]

# def minInsertions(s, p):
#     n = len(s)
#     dp = [[0] * (n + 1) for i in range(n + 1)]
#     for i in range(n):
#         for j in range(n):
#             dp[i + 1][j + 1] = dp[i][j] + p[ord(s[i]) - ord('a')] if s[i] == s[~j] else max(dp[i][j + 1], dp[i + 1][j])
#     return dp[n][n]

# print(minInsertions(s, p))

# n, k = map(int, input().split())
# p = [0] * 26
# for i in range(k):
#     p[ord(input()) - ord('a')] = int(input())
# s = input().strip()

# # Define a function to compute the cost of adding a character to the string
# def cost(i, j):
#     return p[i] if i == j else p[i] + p[j]

# # Initialize the DP table with the base cases
# dp = [[0] * n for _ in range(n)]
# for i in range(n-1):
#     dp[i][i+1] = cost(ord(s[i])-ord('a'), ord(s[i+1])-ord('a'))

# # Compute the remaining subproblems in bottom-up order
# for L in range(4, n+1, 2):
#     for i in range(n-L+1):
#         j = i + L - 1
#         if s[i] == s[j]:
#             dp[i][j] = dp[i+1][j-1]
#         else:
#             dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + cost(ord(s[i])-ord('a'), ord(s[j])-ord('a'))

# # The minimum cost of making the string symmetric is stored in dp[0][n-1]
# print(dp[0][n-1])

# # n, k = map(int, input().split())
# # p = {}
# # for i, c in enumerate(input().split()):
# #     p[chr(ord('a') + i)] = int(c)
# # s = input().strip()

# # dp = [[0] * n for _ in range(n)]
# # for i in range(n-1):
# #     dp[i][i+1] = 0 if s[i] == s[i+1] else min(p[s[i]], p[s[i+1]])

# # for L in range(3, n+1):
# #     for i in range(n-L+1):
# #         j = i + L - 1
# #         if s[i] == s[j]:
# #             dp[i][j] = dp[i+1][j-1]
# #         else:
# #             dp[i][j] = min(dp[i+1][j] + p[s[i]], dp[i][j-1] + p[s[j]])

# # print(dp[0][n-1])
