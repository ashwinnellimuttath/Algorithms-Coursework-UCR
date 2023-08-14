# morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
#               '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
#               '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
#               '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

# strokes_dict = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J': 1,
#                 'K': 2, 'L': 1, 'M': 2, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2,
#                 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}

# f = [0] + [float('inf')] * len('--..--.')
# for i in range(1, len('--..--.')+1):
#     for j in range(i):

#         if '--..--.'[j:i] in morse_dict:
#             f[i] = min(f[i], f[j] + strokes_dict[morse_dict['--..--.'[j:i]]])
#             print(morse_dict['--..--.'[j:i]], strokes_dict[morse_dict['--..--.'[j:i]]])
# print(f[len('--..--.')])

from collections import deque


def longestSubarray(nums, limit = 1) :
        # Example: [10,1,2,4,7,4,3,1], limit = 5
        dqMax, dqMin = deque(), deque()
        ans = 0
        l = 0
        n = len(nums)
        for r in range(n):
            while dqMax and nums[dqMax[-1]] <= nums[r]:  # If we found a larger element then no need to keep smaller elements
                dqMax.pop()
            while dqMin and nums[dqMin[-1]] >= nums[r]:  # If we found a smaller element then no need to keep larger elements
                dqMin.pop()
            dqMax.append(r)
            dqMin.append(r)
            
            while nums[dqMax[0]] - nums[dqMin[0]] > limit:
                l += 1  # Shrink size by moving the left pointer
                if dqMax[0] < l: dqMax.popleft()
                if dqMin[0] < l: dqMin.popleft()
                    
            ans = max(ans, r - l + 1)
            
        return ans

h = [1,3,3,3,4,4,7,8,7,8,7,4,8,7]
print(longestSubarray(h))
n = len(h)
left = 0
right = 0
# max_height = h[0]
# min_height = h[0]
# max_length = 0

# n = len(h)
# left = 0
# max_length = 0
# max_height = h[0]
# min_height = h[0]

# # for right in range(n):
# #     max_height = max(max_height, h[right])
# #     min_height = min(min_height, h[right])
# #     if max_height - min_height > 1:
# #         left += 1
# #         # adjust max_height and min_height using two pointers
# #         if h[left-1] == max_height:
# #             max_height = max(h[left:right+1])
# #         if h[left-1] == min_height:
# #             min_height = min(h[left:right+1])
# #     max_length = max(max_length, right - left + 1)

# # print(max_length)


temp = 1
max_length = 0
prev = False
min_height = h[0]
max_height = h[0]
for i in range(1,len(h)):
    min_height = min(min_height,h[i], h[i-1])
    max_height = max(max_height,h[i], h[i-1])
    if max_height - min_height > 1:
        temp = 1
        min_height = h[i]
        max_height = h[i]
    else:
        temp += 1
    max_length = max(max_length, temp)

print(max_length)

# for i in range(1,len(h)):
#     if abs(h[i] - h[i-1]) < 1:
#         temp += 1
#         prev = False
#         print(temp,"here")
#     elif abs(h[i] - h[i-1]) == 1 and prev == True:
#         temp += 1
#         print(temp)
#         max_length = max(max_length, temp)
#         prev = False
#         temp = 1
#     elif abs(h[i] - h[i-1]) >= 1 and prev == True:
#         temp = 1
#         prev=False
#     # elif abs(h[i] - h[i-1]) <= 1 and prev:
#     #     temp += 1
#     max_length = max(max_length, temp)

# print(max_length)


    # temp = 0
    # min_height = min(min_height,h[i])
    # max_height = max(max_height,h[i])
    # if max_height  - min_height > 1:



# max_length = 0
# max_height = h[0]
# min_height = h[0]
# while right < n-1:
#     right += 1
#     max_height = max(max_height, h[right])
#     min_height = min(min_height, h[right])
#     while max_height - min_height > 1:
#         left += 1
#         max_height = max(h[left:right+1])
#         min_height = min(h[left:right+1])
#     max_length = max(max_length, right - left + 1)

# print( max_length)


# print(longestSubarray([1,3,4,4,7,7,7,8]))