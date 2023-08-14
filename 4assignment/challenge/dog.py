# 5
# 15 3 4 5 20
# n = int(input())
# happiness = list(map(int, input().split()))
# n = int(input())
# happiness = list(map(int, input().split()))
# 13 17 26 14 8 15 12 16
# 7 8 3 5 6 1 4 10 9 2
# happiness = [15,2,10,15,20]
# happiness = [7,8,3,5,6,1,4,10,9,2]
# happiness = [13,17,26,14,8,15,12,16]
# happiness = [15,3,4,5,20]
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build_tree(arr, 0, 0, self.n - 1)
    
    def build_tree(self, arr, tree_idx, left, right):
        if left == right:
            self.tree[tree_idx] = arr[left]
        else:
            mid = (left + right) // 2
            self.build_tree(arr, 2 * tree_idx + 1, left, mid)
            self.build_tree(arr, 2 * tree_idx + 2, mid + 1, right)
            self.tree[tree_idx] = max(self.tree[2 * tree_idx + 1], self.tree[2 * tree_idx + 2])
    
    def update(self, tree_idx, left, right, arr_idx, value):
        if left == right:
            self.tree[tree_idx] = value
        else:
            mid = (left + right) // 2
            if arr_idx <= mid:
                self.update(2 * tree_idx + 1, left, mid, arr_idx, value)
            else:
                self.update(2 * tree_idx + 2, mid + 1, right, arr_idx, value)
            self.tree[tree_idx] = max(self.tree[2 * tree_idx + 1], self.tree[2 * tree_idx + 2])
    
    def query(self, tree_idx, left, right, query_left, query_right):
        if left > query_right or right < query_left:
            return 0
        elif query_left <= left and right <= query_right:
            return self.tree[tree_idx]
        else:
            mid = (left + right) // 2
            left_max = self.query(2 * tree_idx + 1, left, mid, query_left, query_right)
            right_max = self.query(2 * tree_idx + 2, mid + 1, right, query_left, query_right)
            return max(left_max, right_max)
        
def compute_ranks(S):
    sorted_S = sorted(S)
    ranks = [sorted_S.index(x) + 1 for x in S] 
    
    return ranks

def compute_array_A(S):
    n = len(S)
    ranks = compute_ranks(S)
    A = [0] * n
    segment_tree = SegmentTree([0] * n)
    
    for i in range(n):
        rank_i = ranks[i]
        A[rank_i - 1] = S[i] + segment_tree.query(0, 0, n - 1, 0, rank_i - 1)
        segment_tree.update(0, 0, n - 1, rank_i - 1, A[rank_i - 1])
    
    return A,ranks


# Example usage
# n = int(input())
# S = list(map(int, input().split()))
S = [13,17,26,14,8,15,12,16]
# S = [10,1,2,3,4,5,6,7]
A = compute_array_A(S)
A,rank = compute_array_A(S)
print(S)
print(rank)
print(A)

# for i in range(1,len(rank)):
largest = rank[0]
total = [0] * len(rank)
total[0] = A[largest-1]
for i in range(1,len(rank)):
    if rank[i] > largest:
        largest = rank[i]
        total[i] =  S[i] + total[i-1]
    else:
        total[i] = total[i-1]


print(sum(total))



