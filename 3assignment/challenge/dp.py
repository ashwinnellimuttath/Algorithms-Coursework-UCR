m, n = map(int, input().split())
courses = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    p, r, c = courses[i]
    temp = 0
    if c == 0:
        for j in range(m+1):
            # dp[i][j] = dp[i-1][j]
            if j >= p:
                temp= max(dp[i-1][j], dp[i-1][j-p] + r*p)
    else:
        discussion2 = False
        temp1,temp2,temp3 = 0,0,0
        p1, r1,_ = courses[c]
        if (c + 1) < len(courses) and c + 1 != 0:
            discussion2 = True
            p2, r2,_ = courses[c + 1]
        for j in range(m+1):
            # dp[i][j] = dp[i-1][j]
            if j >= p + p1:
                # dp[i][j] = max(dp[i-1][j], dp[i-1][j-p-p1] + r*p + r1*p1)
                temp1 = max(dp[i-1][j], dp[i-1][j-p-p1] + r*p + r1*p1)
            # dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if discussion2:
                if j >= p + p2:
                    print((r,p),(r2,p2),r*p + r2*p2)
                    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-p-p2] + r*p + r2*p2)
                    temp2 = max(dp[i-1][j], dp[i-1][j-p-p2] + r*p + r2*p2)
                # dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j >= p + p1 + p2:
                    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-p-p1-p2] + r*p + r1*p1 + r2*p2)
                    temp3 = max(dp[i-1][j], dp[i-1][j-p-p1-p2] + r*p + r1*p1 + r2*p2)
                # dp[i][j] = max(dp[i][j], dp[i - 1][j])
            print(temp1,temp2,temp3)
            dp[i][j] = max(temp1,temp2, temp3,temp)

# Print the answer
print(dp[n][m])



# m, n = map(int, input().split())
# courses = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

# dp = [[0] * (m + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     pi, ri, ci = courses[i]
#     if ci == 0:
#         for j in range(m + 1):
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - pi] + ri * pi)
#     elif ci == 1:
#         p1, r1, _ = courses[ci]
#         for j in range(m + 1):
#             if j >= pi + p1:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - pi - p1] + ri * pi + r1 * p1)
#             dp[i][j] = max(dp[i][j], dp[i - 1][j])
#     else:
#         p2, r2, _ = courses[ci]
#         for j in range(m + 1):
#             if j >= pi + p2:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - pi - p2] + ri * pi + r2 * p2)
#             dp[i][j] = max(dp[i][j], dp[i - 1][j])

# print(dp[n][m])

def dp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # Fill the first column and row to reduce edge cases
    for i in range(N):
        dp[i][0] = 0
    for c in range(M + 1):
        if weight[0] <= c:
            dp[0][c] = profit[0] 

    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i-1][c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[i-1][c - weight[i]]
            dp[i][c] = max(include, skip)
    return dp[N-1][M]


def dp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # Fill the first column and row to reduce edge cases
    for i in range(N):
        dp[i][0] = 0
    for c in range(M + 1):
        if weight[0] <= c:
            dp[0][c] = (c // weight[0]) * profit[0] 

    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i-1][c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[i][c - weight[i]]
            dp[i][c] = max(include, skip)
    return dp[N-1][M]
