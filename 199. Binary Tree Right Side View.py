# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # recursion
# # T: O(N), S: O(H)
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         seen = {}
#         result = []
#         self.dfs(root, seen, result, 0)
#         return result

#     def dfs(self, node, seen, result, current_level):
#         if node is not None:
#             if current_level not in seen:
#                 seen[current_level] = True
#                 result.append(node.val)

#             if node.right is not None:
#                 self.dfs(node.right, seen, result, current_level + 1)
#             if node.left is not None:
#                 self.dfs(node.left, seen, result, current_level + 1)

# # iteration
# # T: O(N), S: O(W). W~N/2
# from collections import deque
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#         queue = deque([root])
#         result = []
#         while queue:
#             curr_level_count = len(queue)
#             for _ in range(curr_level_count):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
            
#             result.append(node.val)
#         return result 

# recursion 2
# T: O(N), S: O(H)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        self.dfs(root, result, 0)
        return result

    def dfs(self, node, result, level):
        if level == len(result):
            result.append(node.val)
        
        for child in [node.right, node.left]:
            if child:
                self.dfs(child, result, level + 1)

