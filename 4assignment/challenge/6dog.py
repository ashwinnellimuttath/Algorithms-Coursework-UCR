class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)

    def update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = max(self.tree[node], value)
            return
        
        mid = (start + end) // 2
        if index <= mid:
            self.update(2 * node + 1, start, mid, index, value)
        else:
            self.update(2 * node + 2, mid + 1, end, index, value)
        
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, start, end, left, right):
        if start > right or end < left:
            return 0
        if left > right:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        # if left == start and end == right:
        #     return self.tree[node]
        
        mid = (start + end) // 2
        left_query = self.query(2 * node + 1, start, mid, left, right)
        right_query = self.query(2 * node + 2, mid + 1, end, left, right)
        
        return max(left_query, right_query)

def compute_array_A(S):
    n = len(S)
    ranks = compute_ranks(S)
    segment_tree = SegmentTree(n)
    A = [0] * n
    for i in range(n):
        rank_i = ranks[i]
        A[rank_i-1] = S[i] * (n - i) + segment_tree.query(0, 0, n-1, 0, rank_i-1)
        segment_tree.update(0, 0, n-1 , rank_i, A[rank_i-1])
    # return segment_tree.query(0, n - 1, 0, 0, n - 1),ranks
    return segment_tree.query(0, 0, n-1, 0, n-1),A
def compute_ranks(S):
    n = len(S)
    p = [(S[i], i) for i in range(n)]
    p.sort(key=lambda x: (x[0], -x[1]))
    # p.sort()
    indices = {}

    # Populate the dictionary with the indices
    for i, (x, _) in enumerate(p):
        if x not in indices:
            indices[x] = i

    # Get the ranks based on the dictionary
    ranks = [indices[x]+ 1 for x in S]

    return ranks


n = int(input())
S = list(map(int, input().split()))
# S = [10,1,2,3,4,5,6,7]
# S = [7,8,3,5,6,1,4,10,9,2]
# S = [15,3,4,5,20]
A,B = compute_array_A(S)
print(A)
# print(max(B))