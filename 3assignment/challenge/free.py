def binary_search(arr, x,used_days):
    # Initialize low and high indices
    low = len(used_days)
    high = len(arr) - 1
    
    # Binary search algorithm
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

        # while low <= high and arr[low] in used_days:
        #     low += 1
    return low


n, m = map(int, input().split())

yihan_free_days = list(int(input()) for _ in range(n))

students_free_days = []
for i in range(m):
    x, y = map(int, input().split())
    students_free_days.append((x, y))


# print(yihan_free_days)

students_free_days.sort(key=lambda x: (x[1],x[0]))
yihan_free_days.sort()

# print(students_free_days)
# print(yihan_free_days)



max_students = 0
used_days = set()

# for x, y in students_free_days:
#     for day in range(x, y+1):
#         if day in yihan_free_days and day not in used_days:
#             max_students += 1
#             used_days.add(day)
#             break


# for x, y in students_free_days:
#     index = binary_search(yihan_free_days, x,used_days)
#     while index < len(yihan_free_days) and yihan_free_days[index] <= y:
#         print(index)
#         if yihan_free_days[index] not in used_days:
#             max_students += 1
#             used_days.add(yihan_free_days[index])
#             break
#         index += 1

# j = 0
# i = 0
# # for i, (x, y) in enumerate(students_free_days):
# while i < len(yihan_free_days):
#     # if yihan_free_days[j] <= y:
#     val = yihan_free_days[i]
#     x,y = students_free_days[j]
#     if j < len(students_free_days) and val >= x and val <=y :
#         print(x,yihan_free_days[j])
#         max_students += 1
#         # used_days.add(yihan_free_days[j])
#         j +=1
#         i +=1
#         # continue
#     elif j < len(students_free_days) - 1 :
#         j += 1
    # else:
    #     i += 1
        # j +=1
    # elif j < len(yihan_free_days) and y >= yihan_free_days[j] :
    #     j += 1
    # else:
    #     i += 1

# j = 0
# i = 0
# # for i, (x, y) in enumerate(students_free_days):
# while i < len(students_free_days):
#     # if yihan_free_days[j] <= y:
#     x,y = students_free_days[i]
#     if j < len(yihan_free_days) and x <= yihan_free_days[j] and  y >= yihan_free_days[j] :
#         # print(x,yihan_free_days[j])
#         max_students += 1
#         # used_days.add(yihan_free_days[j])
#         j +=1
#         i +=1
#         # continue
#     elif j < len(yihan_free_days) and x > yihan_free_days[j] and y >= yihan_free_days[j] :
#         j += 1
#     else:
#         i += 1

j = 0
i = 0
# for i, (x, y) in enumerate(students_free_days):
while i < len(students_free_days):
    # if yihan_free_days[j] <= y:
    x,y = students_free_days[i]
    if j < len(yihan_free_days) and x <= yihan_free_days[j] <=y  :
        # print(x,yihan_free_days[j])
        max_students += 1
        # used_days.add(yihan_free_days[j])
        j +=1
        i +=1
        # continue
    elif j < len(yihan_free_days) and x > yihan_free_days[j]:
        j += 1
        # i += 1
    else:
        i += 1

    


print(max_students)



# import heapq

# n, m = map(int, input().split())

# yihan_free_days = set(int(input()) for _ in range(n))

# students_free_days = []
# for i in range(m):
#     x, y = map(int, input().split())
#     students_free_days.append((y, x))  # Reversed order to simplify the heap implementation

# max_students = 0
# used_days = set()
# students_heap = []
# for day in sorted(yihan_free_days):
#     # Pop students whose intervals have ended before the current day
#     while students_heap and students_heap[0][0] < day:
#         heapq.heappop(students_heap)
#     # Find the next student whose interval contains the current day
#     while students_free_days and students_free_days[-1][0] >= day:
#         y, x = students_free_days.pop()
#         heapq.heappush(students_heap, (y, x))
#     if students_heap:
#         _, x = heapq.heappop(students_heap)
#         if x <= day and day not in used_days:
#             max_students += 1
#             used_days.add(day)

# print(max_students + 1)


