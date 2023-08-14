n, m = map(int, input().split())

# create a list of courses, where each course is a tuple of its prerequisite and credit
no_prereq_courses = []
prereq_courses = []
for i in range(n):
    p, c = map(int, input().split())
    if p == 0:
        no_prereq_courses.append((i,0, c))
    else:
        prereq_courses.append((i, p-1, c))

# initialize the dp array with zeros
dp = [[(0,0)]*(m+1) for _ in range(n)]

# base case: dp[i][1] is simply the credit of course i
print(no_prereq_courses)
for i in range(len(no_prereq_courses)):
    _,_,c = no_prereq_courses[i]
    dp[i][0] = (c,1)

# for i in range(1,len(no_prereq_courses)+1):
#     idx, pre, c = no_prereq_courses[i]
#     for j in range(1,m+1):
#         if c <= j:
#             dp[i,j] = max(dp[i-1][j],dp[i-1][j-c])



# for i, c in no_prereq_courses:
#     dp[i][1] = (c,1)


# for i in range(1,n+1):
#     for j in range(1,m+1):
#         dp[i,j] = dp[i-1][j]

# # fill in the dp array
# for j in range(2, m+1):
#     for i in range(n):
#         # if course i has no prerequisite
#         if courses[i][0] == 0:
#             dp[i][j] = max(dp[k][j-1] + courses[i][1] for k in range(n) if k != i)
#         # if course i has a prerequisite
#         else:
#             prereq = courses[i][0]-1
#             dp[i][j] = max(dp[k][j-1] + courses[i][1] for k in range(n) if k != i and dp[prereq][j-1] > 0)

# # find the maximum total credit we can get by taking at most m courses
# ans = max(dp[i][m] for i in range(n))

print(dp)
