# M = int(input())
# prices = list(map(int, input().split()))

M = 10
prices = [4, 3, 10, 8, 5, 6, 3, 12, 4]

M = 28
prices = [7, 5, 6, 8, 5, 5, 6, 10, 7]

# age = ""
# for i in range(9, 0, -1):
#     if prices[i-1] <= M:
#         age += str(i)
#         M -= prices[i-1]

# if not age:
#     print(0)
# else:
#     age = ''.join(sorted(age, reverse=True))
#     print(age)

minPrice = min(prices)
max_digit = M//min(prices)

result = ""

# for i in reversed(range(len(prices))):
i = len(prices) - 1
while i >= 0:
    # print(i)
    if prices[i] <= M:
        newM = M - prices[i]
        # print(" ",newM,minPrice,newM//minPrice)
        if newM//minPrice == max_digit - 1:
            result += str(i+1)
            max_digit = newM//minPrice
            M = newM
            i = len(prices) - 1
        else:
            i-= 1
    else:
        i-=1

print(result)


















# M = 28
# prices = [7, 5, 6, 8, 5, 5, 6, 10, 7]


# age = ""
# while M >= min(prices):
#     max_price = max([p for p in prices if p <= M])
#     age += str(prices.index(max_price) + 1)
#     M -= max_price

# print(age)

# digits = [(i+1, prices[i]) for i in range(9)]
# digits.sort(key=lambda x: x[1], reverse=True)

# max_number = ""
# for digit, price in digits:
#     if price <= M:
#         max_number += str(digit) * (M // price)
#         M %= price

# print(max_number if len(max_number) > 0 else "0")
