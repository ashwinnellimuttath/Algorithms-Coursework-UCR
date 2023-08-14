# n = int(input())
# students = []
# total_candies = 0
# for i in range(n):
#     l, a = map(int, input().split())
#     students.append((l, a))
#     total_candies += a

# students.sort()
import heapq


n = 4
students = [(20, 300), (40, 400), (340, 700), (360, 600)]
# total_candies = 2000
lo = 0
hi = 700

# Binary search
while lo < hi:
    mid = (lo + hi) // 2

    # check if each student can have at least mid candies
    candies_needed = [max(0, mid-a) for l, a in students]
    for i in range(n):
        for j in range(i+1, n):
            distance = students[j][0]-students[i][0]
            candies_to_give = min(candies_needed[i], students[j][1]-max(0, distance))
            candies_needed[i] -= candies_to_give
            candies_needed[j] += candies_to_give - abs(students[i][0]-students[j][0])
        
            print(candies_needed)

    if all(c >= 0 for c in candies_needed):
        lo = mid + 1
    else:
        hi = mid - 1

print(lo)




# while lo < hi:
#     mid = (lo + hi) // 2
#     print(mid)

#     # check if each student can have at least mid candies
#     candies_needed = [max(0, mid-a) for l, a in students]
#     print(candies_needed)
#     for i in range(n):
#         for j in range(i):
#             distance = students[i][0]-students[j][0]
#             candies_to_give = min(candies_needed[i], students[i][1]-max(0, distance))
#             candies_needed[j] -= candies_to_give
#             candies_needed[i] += (students[j][1] - mid) + candies_to_give - abs(distance)

#     print(candies_needed)
#     if all(c >= 0 for c in candies_needed):
        
#         lo = mid + 1
#     else:
#         hi = mid - 1

# print(lo)































# while lo < hi:
#     mid = (lo + hi + 1) // 2
#     candies_needed = [max(0, mid - a) for l, a in students]
#     can_redistribute = True
#     for i in range(n-1, 0, -1):
#         j = i - 1
#         candies_to_give = candies_needed[j] - candies_needed[i]
#         distance = students[i][0] - students[j][0]
#         if candies_to_give > students[j][1]:
#             can_redistribute = False
#             break
#         candies_needed[j] -= candies_to_give
#         candies_needed[i] += candies_to_give - distance
#     print(lo)
#     if all(c >= 0 for c in candies_needed) and can_redistribute:
#         lo = mid
#     else:
#         hi = mid - 1

# print(lo)







































# while lo < hi:
#     mid = (lo + hi) // 2
#     print(mid)

#     # check if each student can have at least mid candies
#     candies_needed = [max(0, mid-a) for l, a in students]
#     print(candies_needed)
#     for i in range(n):
#         for j in range(i+1, n):
#             candies_to_give = min(candies_needed[i], students[j][1]-max(0, students[j][0]-students[i][0]))
#             candies_needed[i] -= candies_to_give
#             candies_needed[j] += candies_to_give - abs(students[i][0]-students[j][0])

#     print(candies_needed)
#     if all(c >= 0 for c in candies_needed):
        
#         lo = mid + 1
#     else:
#         hi = mid - 1

# print(lo)




# lo = 0
# hi = max(a for l, a in students)
# low = 0
# high = max(a for l, a in students)
# while low <= high:
#     mid = (low + high) // 2
#     print(mid)
#     pq = []
#     for l, a in students:
#         heapq.heappush(pq, (-a, l))

#     while pq:
#         a, l = heapq.heappop(pq)
#         updated = False
#         for other_a, other_l in pq:
#             dist = abs(l - other_l)
#             transfer = min(a - mid, max(mid - dist, 0))
#             if transfer > 0:
#                 updated = True
#                 a -= transfer
#                 other_a += transfer - dist
#                 heapq.heappush(pq, (-other_a, other_l))
#             if a <= mid:
#                 break
#         if updated:
#             heapq.heappush(pq, (-a, l))
#         if a <= mid:
#             break

#     # Check if all students have at least mid candies
#     if all(-a >= mid for a, _ in pq):
#         low = mid + 1
#     else:
#         high = mid - 1

# print(high)