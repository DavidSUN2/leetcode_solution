# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# solution1: iteration
# T: O(N), S: O(W)
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # output = []
        # if root is None:
        #     return []
        # queue = deque()
        # queue.append(root)
        # local = []
        # level = len(queue)
        # while queue:
        #     node = queue.popleft()
        #     level -= 1
        #     local.append(node.val)
        #     if node.left is not None:
        #         queue.append(node.left)
        #     if node.right is not None:
        #         queue.append(node.right)
        #     if level == 0:
        #         output.append(local)
        #         local = []
        #         level = len(queue)
        # return output
        output = []
        if root is None:
            return []
        queue = deque([root])
        while queue:
            curr_level_count = len(queue)
            output.append([])
            for _ in range(curr_level_count):
                node = queue.popleft()
                output[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return output
# # solution 2: recursion
# # T: O(N), S: O(H) -> O(N)
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         output = []
#         if root is None:
#             return output

#         self.dfs(root, output, 0)
#         return output
        
#     def dfs(self, node: Optional[TreeNode], output: list[list[int]], level: int) -> None:
#         if len(output) == level:
#             output.append([])
#         output[level].append(node.val)

#         if node.left:
#             self.dfs(node.left, output, level + 1)
#         if node.right:
#             self.dfs(node.right, output, level + 1)