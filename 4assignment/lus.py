n = int(input())

sequence = list(map(int, input().split())) 

dp = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j] + 1)

dpD = [1 for i in range(n)]
for i in reversed(range(n-1)): #loop from n-2 downto 0
    for j in reversed(range(i-1 ,n)):
        if sequence[j] < sequence[i]:
            dpD[i] = max(dpD[i], dpD[j] + 1)

maximum = dp[0] + dpD[0] - 1
for i in range(1 , n):
    maximum = max((dp[i] + dpD[i]-1), maximum)
    
print( maximum)



# print(lis_max_sum([1, 3, 6, 5, 4, 8, 10, 3, 2, 6, 4, 9, 7, 6, 4]))