# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pq = []
        def dfs(node):
            if not node:
                return
            heapq.heappush(pq, (node.val, node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        i = 1
        p = 0
        while True:
            if i == k:
                v, p = heapq.heappop(pq)
                break
            else:
                heapq.heappop(pq)
                i = i + 1
                continue
        return p


