class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0] * (4 * n)
        self.build(arr, 0, n-1, 0)

    def build(self, arr, start, end, node):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, start, mid, 2*node + 1)
            self.build(arr, mid+1, end, 2*node + 2)
            self.tree[node] = max(self.tree[2*node + 1], self.tree[2*node + 2])

    def query(self, start, end, node, left, right):
        if left > end or right < start:
            return 0
        elif left <= start and right >= end:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            left_val = self.query(start, mid, 2*node + 1, left, right)
            right_val = self.query(mid+1, end, 2*node + 2, left, right)
            return max(left_val, right_val)

    def update(self, start, end, node, idx, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(start, mid, 2*node + 1, idx, value)
            else:
                self.update(mid+1, end, 2*node + 2, idx, value)
            self.tree[node] = max(self.tree[2*node + 1], self.tree[2*node + 2])


def calculate_highest_happiness(n, toys):
    segment_tree = SegmentTree(toys)
    happiness = [0] * n

    for day in range(n):
        max_funness = segment_tree.query(0, n-1, 0, 0, n-1)
        happiness[day] = max_funness

        # Update the segment tree to remove toys with funness <= max_funness
        for i in range(n):
            if toys[i] <= max_funness:
                segment_tree.update(0, n-1, 0, i, 0)

    return (happiness)


# Example usage
n = 5
toys = [15, 3, 4, 5, 20]
highest_happiness = calculate_highest_happiness(n, toys)
print(highest_happiness)  # Output: 95

# for i in range(dp):


# Example usage