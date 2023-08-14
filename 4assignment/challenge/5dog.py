def compute_ranks(S):
    # Sort the sequence S and get the ranks
    # sorted_S = sorted(S)
    # ranks = [sorted_S.index(x) + 1 for x in S]  # Adding 1 to make ranks 1-based

    p = [(S[i], i) for i in range(len(S))]
    p.sort(key=lambda x: (x[0], -x[1]))
    indices = {}
    
    # Populate the dictionary with the indices
    for i, (x, _) in enumerate(p):
        if x not in indices:
            indices[x] = i
    
    # Get the ranks based on the dictionary
    ranks = [indices[x] + 1 for x in S]
    
    return ranks

# def compute_array_A(S):
#     n = len(S)
#     ranks = compute_ranks(S)
#     A = [0] * n
#     for i in range(n):
#         rank_i = ranks[i]
#         A[rank_i - 1] = S[i] * (n-i) + max(A[:rank_i])
#     return A,ranks

class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.max_value = 0
        self.left = None
        self.right = None


def build_segment_tree(nums, start, end):
    if start > end:
        return None

    root = SegmentTreeNode(start, end)

    if start == end:
        root.max_value = nums[start]
        return root

    mid = (start + end) // 2
    root.left = build_segment_tree(nums, start, mid)
    root.right = build_segment_tree(nums, mid + 1, end)
    root.max_value = max(root.left.max_value, root.right.max_value)

    return root


def update_segment_tree(root, index, value):
    if root is None or index < root.start or index > root.end:
        return

    if root.start == root.end == index:
        root.max_value = value
        return

    mid = (root.start + root.end) // 2
    if index <= mid:
        update_segment_tree(root.left, index, value)
    else:
        update_segment_tree(root.right, index, value)

    root.max_value = max(root.left.max_value, root.right.max_value)


def query_segment_tree(root, start, end):
    if root is None or end < root.start or start > root.end:
        return 0

    if start <= root.start and end >= root.end:
        return root.max_value

    return max(query_segment_tree(root.left, start, end), query_segment_tree(root.right, start, end))


def compute_array_A(S):
    n = len(S)
    ranks = compute_ranks(S)

    # Build the segment tree with initial values of 0
    segment_tree = build_segment_tree([0] * n, 0, n - 1)

    A = [0] * n
    for i in range(n):
        rank_i = ranks[i]
        A[rank_i - 1] = S[i] * (n - i) + query_segment_tree(segment_tree, 0, rank_i - 1)

        # Update the segment tree with the new value
        update_segment_tree(segment_tree, rank_i - 1, A[rank_i - 1])

    return A, ranks


# Example usage
# S = [15,3,4,5,20]
# S = [13,17,26,14,8,15,12,16]
n = int(input())
S = list(map(int, input().split()))
# S = [10,1,2,3,4,5,6,7]
# S = [7,8,3,5,6,1,4,10,9,2]
# S = [15,3,4,5,20]
A,rank = compute_array_A(S)
print(max(A))

# for i in range(1,len(rank)):
# largest = rank[0]
# total = [0] * len(rank)
# total[0] = A[largest-1]
# for i in range(1,len(rank)):
#     print(rank[i])
#     if rank[i] > largest:
#         largest = rank[i]
#         total[i] =  S[i] + total[i-1]
#     else:
#         total[i] = total[i-1]


# print(total)
