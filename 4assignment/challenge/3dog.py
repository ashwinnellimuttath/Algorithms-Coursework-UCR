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
            self.update(2 * node, start, mid, index, value)
        else:
            self.update(2 * node + 1, mid + 1, end, index, value)

        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, left, right):
        if start > right or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_val = self.query(2 * node, start, mid, left, right)
        right_val = self.query(2 * node + 1, mid + 1, end, left, right)

        return max(left_val, right_val)

def compute_ranks(S):
    # Sort the sequence S and get the ranks
    # sorted_S = sorted(S)
    # ranks = [sorted_S.index(x) + 1 for x in S]  # Adding 1 to make ranks 1-based

    p = [(S[i], i) for i in range(n)]
    p.sort(key=lambda x: (x[0], -x[1]))
    indices = {}
    
    for i, (x, _) in enumerate(p):
        if x not in indices:
            indices[x] = i
    
    ranks = [indices[x] + 1 for x in S]
    
    return ranks

def compute_array_A(S):
    n = len(S)
    ranks = compute_ranks(S)
    A = [0] * n
    segment_tree = SegmentTree(n)

    for i in range(n):
        rank_i = ranks[i]
        A[rank_i - 1] = S[i] * (n - i) + segment_tree.query(1, 1, n, 1, rank_i - 1)
        segment_tree.update(1, 1, n, rank_i, A[rank_i - 1])
    return segment_tree.query(1, 1, n, 1, n)

# S = [15,3,4,5,20]
S = [13, 17, 26, 14, 8, 15, 12, 16]
n = int(input())
S = list(map(int, input().split()))
A = compute_array_A(S)
print(A)
# print(max(A))

