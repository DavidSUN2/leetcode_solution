# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # solution 1: inorder dfs
# # T: O(N), S: O(logN)
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return True
#         values = []
#         return self.dfs(root, values)

#     def dfs(self, node: Optional[TreeNode], values: list[int]) -> bool:
#         if node is not None:
#             if not self.dfs(node.left, values):
#                 return False
#             if len(values) > 0:
#                 if node.val <= values[-1]:
#                     return False
#                 values[0] = node.val
#             else:
#                 values.append(node.val)
#             if not self.dfs(node.right, values):
#                 return False
#         return True

# # solution 2: bfs
# # T: O(N), S: O(W)
# from collections import deque
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         queue = deque([[root, -float('inf'), float('inf')]])

#         while(queue):
#             current_level_count = len(queue)
#             for _ in range(current_level_count):
#                 node, lower_bound, upper_bound = queue.popleft()
#                 if node.val <= lower_bound or node.val >= upper_bound:
#                     return False
#                 if node.left:
#                     queue.append([node.left, lower_bound, node.val])
#                 if node.right:
#                     queue.append([node.right, node.val, upper_bound])
#         return True
        
# solution 3: preorder dfs
# T: O(N), S: O(logN)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower_bound = -float('inf')
        upper_bound = float('inf')
        return self.dfs(root, lower_bound, upper_bound)

    def dfs(self, node: Optional[TreeNode], lower_bound: int, upper_bound: int) -> bool:
        if node is None:
            return True
        if node.val >= upper_bound or node.val <= lower_bound:
            return False
        return self.dfs(node.left, lower_bound, node.val) and self.dfs(node.right, node.val, upper_bound)