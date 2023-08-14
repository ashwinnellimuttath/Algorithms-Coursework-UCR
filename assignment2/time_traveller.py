# n, k = map(int, input().split())

# classes = []
# for i in range(n):
#     s, t = map(int, input().split())
#     classes.append((s, t))

# classes.sort(key=lambda x: x[1])

# cnt = 0
# for i in range(k+1):
#     if i > 0:
#         classes = [c for c in classes if c[1] > prevEnd]
#     prevEnd = -1
#     for j in range(len(classes)):
#         if classes[j][0] > prevEnd:
#             print(classes[j])
#             cnt += 1
#             prevEnd = classes[j][1]
#     if cnt == n:
#         break

# print(cnt)





# n, k = map(int, input().split())

# classes = []
# for i in range(n):
#     s, t = map(int, input().split())
#     classes.append((s, t))

# classes.sort(key=lambda x: x[1])  # Sort by end time

# print(classes)
# count = 0
# # hashMap = {classes[0][0]-classes[0][1]}
# for i in range(1,len(classes)):
#     sPrev, tPrev = classes[i]
#     s,t = classes[i]
#     if s >= tPrev + 1:
#         count += 1

# totalLeft = len(classes) - n

# print(totalLeft)
        # hashMap[]


def swap(i,j,current):
    current[i], current[j] = current[j], current[i]

n, k = map(int, input().split())

classes = []
for i in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))

classes.sort(key=lambda x: (x[1],x[0])) 
# print(classes)

last_end = 0
count = 0


current = classes[:]

while k >= 0:
    i = 0
    new = []
    last_end = 0
    print(current)
    lastAdded = []
    while i < len(current):
        s,t = current[i]
        if s >= last_end + 1 or i == 0:
            j = i + 1
            if j == len(current) - 1 and k >0:
                sj,tj = current[j]
                if sj < s and sj > lastAdded[1]:
                    # print(sj,tj,s, "here")
                    new.append(current[i])
                    # swap(i,j,current) 
                    i += 2
                    count += 1
                    # last_end = tj
                    continue
            # print(s,t,"here")
            # if last_end > 0:
            lastAdded = current[i]
            count += 1
            last_end = t

        else:
            new.append(current[i])
        i += 1

    current = new
    # i = 0
    # print(new)
    k -= 1
print(count)



# while k >= 0:
#     i = 0
#     new = []
#     last_end = 0
#     while i < len(current):
#         s,t = current[i]
#         if s >= last_end + 1 or i == 0:
#             count += 1
#             last_end = t
#             lastAdded = [current[i]]
#         elif t == lastAdded[-1][1]:
#             lastAdded.append(current[i])
#         elif s < lastAdded[-1][0]:
#             if s >= last_end + 1:
#                 count += 1
#                 last_end = t
#                 lastAdded = [current[i]]
#             else:
#                 new.append(current[i])
#         else:
#             new.append(current[i])
#         i += 1
#     current = new
#     k -= 1
# print(count)



# n, k = map(int, input().split())
# classes = []
# for i in range(n):
#     s, t = map(int, input().split())
#     classes.append((s, t))

# # Sort the classes by end time, so we can use binary search later
# classes.sort(key=lambda x: x[1])

# # Define the dp array
# dp = [[0] * (k+1) for _ in range(n+1)]

# # Fill in the dp array using dynamic programming
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         # Compute the maximum number of classes we can attend before the i-th class
#         # with j turns of the time-turner, such that the last class ends before the i-th class starts
#         left, right = 0, i-1
#         while left <= right:
#             mid = (left + right) // 2
#             if classes[mid][1] + 1 <= classes[i-1][0]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         dp[i][j] = max(dp[i-1][j], dp[left][j-1] + i - left)

# # Print the answer
# print(dp[n][k])
# while k >= 0:
#     i = 0
#     new = []
#     last_end = 0
#     lastAdded = []
#     while i < len(current):
#         s,t = current[i]
#         if s >= last_end + 1 or (lastAdded and t <= lastAdded[-1][1] and s >= lastAdded[-1][0]):
#             count += 1
#             last_end = t
#             lastAdded.append(current[i])
#         else:
#             new.append(current[i])
#         i += 1
#     current = new
#     k -= 1
# print(count)