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
                # temp= max(temp,dp[i-1][j], dp[i-1][j-p] + r*p)
                temp= dp[i-1][j-p] + r*p
                # if i == 6:
                    # print(p,temp,dp[i-1][j-p],"here")
            if temp == 260:
                print("here ")
            # print(temp)
        maxTemp = 0
        discussion1 = False
        if (i + 1) < len(courses) and courses[i+1][2] != 0:
            discussion2 = False
            temp1,temp2,temp3 = 0,0,0
            p1,r1,p2,r2 = 0,0,0,0
            p1, r1,_ = courses[i+1]
            if (i + 2) < len(courses) and courses[i+2][2] != 0:
                discussion2 = True
                p2, r2,_ = courses[i+2]
            for j in range(m+1):
                # dp[i][j] = dp[i-1][j]
                if j >= p + p1:
                    # print("here", (r,p), (r1,p1),r*p + r1*p1)
                    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-p-p1] + r*p + r1*p1)
                    # temp1 = max(dp[i-1][j], dp[i-1][j-p-p1] + r*p + r1*p1)
                    temp1 = dp[i-1][j-p-p1] + r*p + r1*p1
                # dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if discussion2:
                    if j >= p + p2:
                        # print("here2",p + p2,(r,p),(r2,p2),r*p + r2*p2)
                        # dp[i][j] = max(dp[i-1][j], dp[i-1][j-p-p2] + r*p + r2*p2)
                        # temp2 = max(dp[i-1][j], dp[i-1][j-p-p2] + r*p + r2*p2)
                        temp2 = dp[i-1][j-p-p2] + r*p + r2*p2
                    # dp[i][j] = max(dp[i][j], dp[i - 1][j])
                    if j >= p + p1 + p2:
                        # dp[i][j] = max(dp[i-1][j], dp[i-1][j-p-p1-p2] + r*p + r1*p1 + r2*p2)
                        # temp3 = max(dp[i-1][j], dp[i-1][j-p-p1-p2] + r*p + r1*p1 + r2*p2)
                        temp3 = dp[i-1][j-p-p1-p2] + r*p + r1*p1 + r2*p2
                    # dp[i][j] = max(dp[i][j], dp[i - 1][j])
                # print(temp1,temp2,temp3,temp)
                # print((p,r),(p1,r1),(p2,r2))
                maxTemp = max(maxTemp,temp1,temp2,temp3,temp )
                dp[i][j] = max(dp[i-1][j],maxTemp)
                # print(maxTemp)
    # if temp == 260:
    #     print(maxTemp,temp,dp[i-1][j],"heree")
    # dp[i][j] = max(maxTemp,temp,dp[i-1][j])
    print(dp[i][j],i,dp[i-1][j])

# Print the answer
print(dp[n][m])