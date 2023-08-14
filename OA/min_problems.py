threshold = 402
points = [25,162,206,224,264,288,334,364,367,389,405,454,478,479,482,509,517,545,578,626,657,692,705,720,734,747]

def find_binary(points, low, high, key, ans):
    if(low<high):
        mid = (low + high)//2;
        if(points[mid]==key):
            ans = mid
            return
        elif(points[mid]>=key):
            ans = min(ans,mid);
            find_binary(points, low, mid-1,key,ans);
        else:
            find_binary(points, mid+1, high, key, ans);
        
def minNum(threshold, points):
    if (threshold + points[0] > points[len(points)-1]):
        return len(points)
    key = threshold + points[0]
    ans = len(points)-1
    find_binary(points,0,len(points)-1,key,ans)
    ans = ans + 1
    
    _ans = (ans + 2)//2
    return _ans
# print(minNum(2,[1,2,3]))


print(minNum(threshold, points))


# threshold = 4
# points = [1,2,3,5,8]
# num = 1
# n = len(points)
# added = []
# runningSum = 0
# i = 0
# while i < len(points):
#     if added and added[-1] - points[0] >= threshold:
#         print(num)
#         break
#     if n - i > 2:
#         print("here",i)
#         added.append(points[i + 2])
#         # runningSum += points[i + 2]
#         num += 1
#         i += 2
#     elif n-i > 1:
#         print("here1",i)
#         added.append(points[i+1])
#         # runningSum += points[i + 1]
#         num += 1
#         i += 1

# print(n,"here",added)
