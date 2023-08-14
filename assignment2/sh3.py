def is_possible(mid, students):
    candies = [ai for _, ai in students]
    n = len(students)
    d = mid
    
    # students.sort()


    continueDistance = 0
    notNeedMaxSum = 0
    for i in range(1,n):
        distance = students[i][0]-students[i-1][0]
        need = max(0,mid - candies[i-1])
        if not need:
            continueDistance += students[i][0]-students[i-1][0]
            notNeedMaxSum += candies[i-1] - mid
            candies[i] += max(0,candies[i-1] - mid - distance)
            # basket = max(candies[i] - mid - distance,basket)

            continue
        # value = need - distance
        candies[i-1] += (need)

        # if notNeedMaxSum > need:
        #     if students[i-1][0]-students[i-2][0] < students[i][0]-students[i-1][0]:
        #         if notNeedMaxSum - students[i-1][0]-students[i-2][0] > need:
        #             candies[i-2] -= (need + students[i-1][0]-students[i-2][0])
        #             notNeedMaxSum = 0
        #             continue

        candies[i] -= (need + distance)

    # if candies[-1] < mid:
    #     candies[-1] = candies[-1] + notNeedMaxSum - continueDistance
    # print(mid)
    # if mid == 333:
    #     print(candies)
    
    return all(c >= mid for c in candies)


def maximum_candies(students):
    lo = 0
    hi = max(ai for _, ai in students)
    
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if is_possible(mid, students):
            lo = mid 
        else:
            hi = mid - 1
    
    return lo


n = int(input())
students = []
for i in range(n):
    li, ai = map(int, input().split())
    students.append((li, ai))
print(maximum_candies(students))

# n = 4
# students = [(20, 300), (40, 400), (340, 700), (360, 600)]




# def is_possible(mid, students):
#     candies = [ai for _, ai in students]
#     n = len(students)
#     # students.sort()

#     maxCandiesLeft = 0    
#     continueDistance = 0
#     for i in range(1,n):
#         distance = students[i][0]-students[i-1][0]
#         need = max(0,mid - candies[i-1])
#         if not need:
#             continueDistance += students[i][0]-students[i-1][0]
#             continue
#         # value = need - distance
#         candies[i-1] += (need)
#         candies[i] -= (need + distance)


#     if candies[-1] < mid:
#         candies[-1] = candies[-1] + maxCandiesLeft - mid - continueDistance
    
#     return all(c >= mid for c in candies)