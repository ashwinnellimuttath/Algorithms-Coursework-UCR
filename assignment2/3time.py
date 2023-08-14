n, k = map(int, input().split())

classes = []
for i in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))

# print(classes)

# classes = [(4, 6), (1, 10), (6, 9), (7, 8), (2, 4), (1, 10)]
# k = 1





def schedule_intervals(intervals, k):
    # Sort intervals by their ending time
    intervals.sort(key=lambda x: (x[1],x[0]))

    # Initialize resources with sentinel intervals
    resources = [(-float('inf'), -float('inf'))] * k
    # resources = [(0,0)] * k
    
    # Keep track of the number of scheduled intervals
    count = 0
    
    for interval in intervals:
        start, end = interval
        
        # Skip interval if it cannot fit in any resource
        # if res[1] == -float("inf") else start < res[1] + 1 
        # print(start,"start",resources)
        if all(start <= res[1] for res in resources):
            continue
        
        # Choose resource to use
        # for i in range(k):
        #     if end <= resources[i][1] :
        #         resources[i] = interval
        #         break
        # else:
            # Replace resource with latest ending time
        latest = max((r for r in resources if r[1] < start), key=lambda x: x[1])
        # a = ((r for r in resources if r[1] < start))
        # a = resources.sort(key=lambda x: x[1])
        # print(max(resources),"aaaa")
        print(latest,"latest",resources.index(latest))
        resources[resources.index(latest)] = interval

        
        # Increment count for each scheduled interval
        print(resources)
        count += 1
        # print((start,end),"start - end")
    # print(resources)
    
    # Return the number of scheduled intervals
    return count

print(schedule_intervals(classes,k + 1))





def schedule_intervals(intervals,k):
    # Sort intervals by their ending time
    intervals.sort(key=lambda x: x[1])
    
    # Initialize resources with sentinel intervals
    res1, res2 = [(-float('inf'), -float('inf'))] * 2
    count = 0
    
    for interval in intervals:
        start, end = interval
        
        # Skip interval if it cannot fit in any resource
        if start < res1[1]  and start < res2[1] :
            continue
        
        # Choose resource to use
        # if end > res1[1] and end > res2[1]:
        #     if res1[1] < res2[1]:
        #         res1 = interval
        #     else:
        #         res2 = interval
        # elif end > res1[1]:
        #     res1 = interval
        # elif end > res2[1]:
        #     res2 = interval
        if end <= res1[1]:
            res1 = interval
            # print(res1, "here")
        elif end <= res2[1]:

            res2 = interval
            # print(res2, "here")
        else:
            # Replace resource with latest ending time
            # print("HEre")
            # if end > res1[1] and end > res2[1]:
            if res1[1] < res2[1]:
                res1 = interval
            else:
                res2 = interval
        count += 1
        print((res1,res2,"res1 - 2"))
    
    # Check if all intervals were scheduled
    
    return count

# print(schedule_intervals(classes,k))


# def count_assigned_intervals(intervals):
#     """
#     Given a list of intervals as tuples (start_time, end_time), returns the count
#     of intervals that can be assigned to resources using the Greedy algorithm.
#     """
#     # Sort intervals by ending time
#     intervals.sort(key=lambda x: x[1])

#     # Initialize resources with sentinel intervals
#     resource1 = (-float('inf'), -float('inf'))
#     resource2 = (-float('inf'), -float('inf'))

#     # Initialize latest end time for each resource
#     latest_end_time1 = -float('inf')
#     latest_end_time2 = -float('inf')

#     # Iterate over intervals and assign to resources
#     count = 0
#     for interval in intervals:
#         start_time, end_time = interval

#         # Calculate minimum start time for next class
#         next_class_start_time = max(latest_end_time1, latest_end_time2) + 1

#         # If interval starts before minimum start time, skip it
#         if start_time < next_class_start_time:
#             continue

#         # If interval starts before both resource endpoints, skip it
#         if start_time < resource1[1] and start_time < resource2[1]:
#             continue

#         # Choose the resource whose endpoint is latest and still before start_time
#         if end_time > resource1[1] and end_time > resource2[1]:
#             if resource1[1] < resource2[1]:
#                 resource1 = interval
#             else:
#                 resource2 = interval
#         elif end_time > resource1[1]:
#             resource1 = interval
#         elif end_time > resource2[1]:
#             resource2 = interval

#         # Update latest end time for assigned resource
#         if resource1 == interval:
#             latest_end_time1 = end_time
#         elif resource2 == interval:
#             latest_end_time2 = end_time

#         count += 1

#     # Return the count of assigned intervals
#     return count

# count = count_assigned_intervals(classes)
# print(count)

# def schedule_intervals(intervals, k):
#     # Sort intervals by their ending time
#     intervals.sort(key=lambda x: x[1])
    
#     # Initialize resources with sentinel intervals
#     resources = [[(-float('inf'), -float('inf'))] * (k + 1)][0]

#     print(resources)
    
#     # Keep track of the number of scheduled intervals
#     count = 0
    
#     for interval in intervals:
#         start, end = interval
        
#         # Skip interval if it cannot fit in any resource
#         if all(start < res[1] for res in resources):
#             continue
        
#         # Choose resource to use
#         assigned = False
#         for i in range(k):
#             if end <= resources[i][1]:
#                 resources[i] = interval
#                 assigned = True
#                 break
        
#         # Replace resource with latest ending time
#         if not assigned:
#             max_end = max(res[1] for res in resources)
#             for i in range(k):
#                 if resources[i][1] == max_end:
#                     resources[i] = interval
#                     break
        
#         # Increment count for each scheduled interval
#         count += 1
    
#     # Return the number of scheduled intervals
#     return count




# def count_assigned_intervals(intervals):
#     """
#     Given a list of intervals as tuples (start_time, end_time), returns the count
#     of intervals that can be assigned to resources using the Greedy algorithm.
#     """
#     # Sort intervals by ending time
#     intervals.sort(key=lambda x: x[1])

#     # Initialize resources with sentinel intervals
#     resource1 = (-float('inf'), -float('inf'))
#     resource2 = (-float('inf'), -float('inf'))

#     # Iterate over intervals and assign to resources
#     count = 0
#     for interval in intervals:
#         start_time, end_time = interval

#         # If interval starts before both resource endpoints, skip it
#         if start_time < resource1[1] and start_time < resource2[1]:
#             continue

#         # Choose the resource whose endpoint is latest and still before start_time
#         if end_time > resource1[1] and end_time > resource2[1]:
#             if resource1[1] < resource2[1]:
#                 resource1 = interval
#             else:
#                 resource2 = interval
#         elif end_time > resource1[1]:
#             resource1 = interval
#         elif end_time > resource2[1]:
#             resource2 = interval

#         count += 1

#     # Return the count of assigned intervals
#     return count

# count = count_assigned_intervals(classes)
# print(count)

# def max_classes(n, k, classes):
#     # Sort classes by end time
#     classes.sort(key=lambda x: x[1])
    
#     # Initialize table for dynamic programming
#     table = [[0] * (k+1) for _ in range(n)]
    
#     # Base case: no classes or no turns
#     for j in range(k+1):
#         table[0][j] = 1 if j == 0 else 0
    
#     # Fill table using dynamic programming
#     for i in range(1, n):
#         for j in range(k+1):
#             # Option 1: don't attend class i
#             table[i][j] = table[i-1][j]
            
#             # Option 2: attend class i and go back in time
#             for t in range(i-1, -1, -1):
#                 if classes[t][1] + 1 + j < classes[i][0]:
#                     table[i][j] = max(table[i][j], 1 + table[t][j+1])
#                 else:
#                     break
    
#     # Return maximum number of classes that can be attended
#     return table[n-1][0]




# n, k = map(int, input().split())

# classes = []
# for i in range(n):
#     s, t = map(int, input().split())
#     classes.append((s, t))

# print(max_classes(n,k,classes))

# classes.sort(key=lambda x: (x[1],x[0])) 
# # print(classes)

# last_end = 0
# count = 0


# def backtrack(current, k, last_end):
#     global count
#     # Base case: no more turns left or no more classes to attend
#     if k == 0 or not current:
#         return

#     # Choose a class to attend
#     for i, (s, t) in enumerate(current):
#         if s >= last_end + 1:
#             # Attend this class
#             count += 1
#             last_end = t
#             chosen_class = current.pop(i)

#             # Recursive call with k-1 turns left and the remaining classes
#             backtrack(current, k-1, last_end)

#             # Backtrack: undo the choice and add the class back to the current list
#             current.insert(i, chosen_class)
#             last_end = max(class_[1] for class_ in current if class_[0] >= last_end + 1)
#             # If the last_end value has changed, it means some classes that were skipped before
#             # can now be attended, so we need to backtrack and try other choices as well.
#             if last_end > t:
#                 backtrack(current, k-1, last_end)
#             break

# current = classes[:]
# backtrack(current, k, last_end)

# print(count)
