m, n = map(int, input().split())
main_courses = []
discussion_courses = {}

for i in range(1, n+1):
    pi, ri, ci = map(int, input().split())
    if ci == 0:
        main_courses.append((pi, ri,i))
    else:
        if ci not in discussion_courses:
            discussion_courses[ci] = []
        discussion_courses[ci].append((pi, ri, i))

courses = [(0, 0, 0)] + main_courses
dp = [[0] * (m + 1) for _ in range(len(courses) + 1)]

for i in range(1, len(courses)):
    p, r, c = courses[i]
    temp = 0
    for j in range(1,m+1):
        # if c != 0:
        #     dp[i][j] = dp[i-1][j]
        maxTemp = 0
    # if c == 0:
    # print(j)
    # dp[i][j] = dp[i-1][j]
        if j >= p:
            # temp= max(temp,dp[i-1][j], dp[i-1][j-p] + r*p)
            temp= dp[i-1][j-p] + r*p
            # if i == 6:
            #     print(p,temp,dp[i-1][j-p],"here")
            # print("here ",temp)
            # print(temp)
        # if temp == 260:
        maxTemp = 0
        discussion1 = False
        temp1,temp2,temp3 = 0,0,0
        p1,r1,p2,r2 = 0,0,0,0

        if c in discussion_courses:
            dCourses = discussion_courses[c]
            # print(dCourses,i)

            discussion2 = False
            p1, r1,_ = dCourses[0]
            if len(dCourses) > 1:
                discussion2 = True
                p2, r2,_ = dCourses[1]
            # dp[i][j] = dp[i-1][j]
            if j >= p + p1:
                # print("here", (r,p), (r1,p1),r*p + r1*p1)
                # dp[i][j] = max(dp[i-1][j], dp[i-1][j-p-p1] + r*p + r1*p1)
                # temp1 = max(dp[i-1][j], dp[i-1][j-p-p1] + r*p + r1*p1)
                temp1 = dp[i-1][j-p-p1] + r*p + r1*p1
                # print(temp1,"temp1",p1,r1 )
            # dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if discussion2:
                if j >= p + p2:
                    # print("here2",p + p2,(r,p),(r2,p2),r*p + r2*p2)
                    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-p-p2] + r*p + r2*p2)
                    # temp2 = max(dp[i-1][j], dp[i-1][j-p-p2] + r*p + r2*p2)
                    temp2 = dp[i-1][j-p-p2] + r*p + r2*p2
                    # print(temp2,"temp1")

                # dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j >= p + p1 + p2:
                    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-p-p1-p2] + r*p + r1*p1 + r2*p2)
                    # temp3 = max(dp[i-1][j], dp[i-1][j-p-p1-p2] + r*p + r1*p1 + r2*p2)
                    temp3 = dp[i-1][j-p-p1-p2] + r*p + r1*p1 + r2*p2
                # dp[i][j] = max(dp[i][j], dp[i - 1][j])
            # print(temp1,temp2,temp3,temp)
            # print((p,r),(p1,r1),(p2,r2))
        maxTemp = max(maxTemp,temp1,temp2,temp3,temp )
        # print(maxTemp,temp1,temp2,temp3,temp)
        dp[i][j] = max(dp[i-1][j],maxTemp)
    # print(dp[i][j],i,dp[i-1][j])
                # print(maxTemp)
    # if temp == 260:
    #     print(maxTemp,temp,dp[i-1][j],"heree")
    # dp[i][j] = max(maxTemp,temp,dp[i-1][j])

# Print the answer
print(dp[len(courses)-1][m])
# print(dp[len(courses)-1][m])

# m, n = map(int, input().split())
# courses = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

# dp = [[0] * (m + 1) for _ in range(n + 1)]

# for i in range(1, n+1):
#     p, r, c = courses[i]
#     temp = 0
#     if c == 0:
#         for j in range(1,m+1):
#             if j >= p:
#                 temp= dp[i-1][j-p] + r*p
#             dp[i][j] = max(dp[i-1][j], temp)

#     if c != 0:
#         pmain,rmain,_ = courses[c]
#         for j in range(1,m+1):
#             if j >= pmain + p:
#                 temp1 = dp[i-1][j-p-pmain] + r*p + pmain*rmain
#             dp[i][j] = max(dp[i-1][j], temp)
#     # print(dp[i][j],i,dp[i-1][j])
        
    
# print(dp)
        