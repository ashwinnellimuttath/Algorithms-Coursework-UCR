

# def lis_max_sum(arr):
#     nums = [4, 1, 2, 5, 3]
#     sumArray = nums[:]
#     max_sum = nums[0] 
#     longest = [1] * len(nums)

#     for i in range(len(nums),-1,-1):
#         for j in range(i + 1,len(nums)):
#             if nums[i] < nums[j]:
#                 longest[i] = max(longest[i], 1 + (longest[j]))

#     return max(longest)

# m = int(input())
# arr = list(map(int, input().split()))
# arr = [1, 3, 6, 5, 4, 8, 10, 3, 2, 6, 4, 9, 7, 6, 4]
# # arr = [4,1,2,5,3]

# n = len(arr)
# print(n)
# L = [1] * n 
# S = arr[:]  
# max_sum = float("-inf")  

# for i in range(len(arr),-1,-1):
#     # print(i)
#     for j in range(i, len(arr)):
#         print(i,j)
#         if arr[i] < arr[j] and L[j] + 1 > L[i]:
#             L[i] = L[j] + 1
#             S[i] = S[j] + arr[i]
#             if S[i] > max_sum:
#                 max_sum = S[i]
# print(max_sum)

n = int(input())
happiness = list(map(int, input().split()))

dp = [happiness[i] for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if happiness[j] < happiness[i]:
            dp[i] = max(dp[i], dp[j] + happiness[i])

print(max(dp))

# print(lis_max_sum([1, 3, 6, 5, 4, 8, 10, 3, 2, 6, 4, 9, 7, 6, 4]))