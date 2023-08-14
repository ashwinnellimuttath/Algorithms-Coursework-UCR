

m = 10
prices = [4, 3, 10, 8, 5, 6, 3, 12, 4]
# m = 28
# prices = [7, 5, 6, 8, 5, 5, 6, 10, 7]

memo = [-1] * (m+1)

def solve(price):
    if memo[price] != -1:
        return memo[price]
    if price == 0:
        return 0
    ans = 0
    for i in range(1, 10):
        if prices[i-1] <= price:
            temp = solve(price-prices[i-1])
            if temp != 0 or i == 1:
                ans = max(ans, int(str(i) + str(temp)))
    memo[price] = ans
    return ans

dp = solve(m)
print(dp,memo)

# dp = [0] * (m + 1)
# for p in prices:
#     for i in range(p, m+1):
#         dp[i] = max(dp[i], int(str(p) + str(dp[i-p])))

# print(dp)

# m = int(input())
# prices = list(map(int, input().split()))



# result = ''
# for i in range(9, 0, -1):
#     if prices[i-1] <= m:
#         result += str(i)
#         m -= prices[i-1]
#         print(m)

# print(result)

# dp = [''] * (m+1)
# for i in range(1, m+1):
#     max_num = ''
#     for j in range(1, 10):
#         if i >= prices[j-1]:
#             num = str(j) + dp[i-prices[j-1]]
#             if int(num) > int(max_num):
#                 max_num = num
#     dp[i] = max_num

# print(dp[m])

# result = ''
# while m > -1:
#     max_digit = -1
#     for i in range(9, 0, -1):
#         if prices[i-1] <= m:
#             max_digit = i
#             break
#     if max_digit == -1:
#         break
#     result += str(max_digit)
#     m -= prices[max_digit-1]
#     print(m)

# print(result)

# result = ''
# while m > 0:
#     max_price = -1
#     max_digit = -1
#     for i in range(9):
#         if prices[i] <= m and prices[i] > max_price:
#             max_price = prices[i]
#             max_digit = i + 1
#     if max_digit == -1:
#         break
#     result += str(max_digit)
#     m -= max_price

# print(result)

# import heapq
# money = 28
# cost = [7, 5, 6, 8, 5, 5, 6, 10, 7]

# heapq.heapify(cost)

# for c in cost:
#     current = heapq.heappop(cost)
    