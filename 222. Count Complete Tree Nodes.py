# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # brute force recursion: dfs
# # T: O(N), S: O(H)
# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         node_count = 0
#         return self.dfs(root, node_count)

#     def dfs(self, node: TreeNode, node_count: int) -> int:
#         if node is None:
#             return node_count
#         node_count += 1
#         node_count = self.dfs(node.left, node_count)
#         node_count = self.dfs(node.right, node_count)
#         return node_count

# # brute force iteration: bfs
# # T: O(N), S: O(W)
# from collections import deque
# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         node_count = 0
#         queue = deque([root])
#         while queue:
#             node = queue.popleft()
#             node_count += 1
#             for child in [node.left, node.right]:
#                 if child:
#                     queue.append(child)
        
#         return node_count


# step 1: check height (0-indexed)
# step 2: index leaves/last row
# step 2: verify whether the node with mid index exists or not
# T: O(logn^2), S: O(logn) or O(1)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        height = self.get_height(root)
        if height == 0:
            return 0
        # return self.get_nodes_count(root, height, 0, 2 ** (height - 1) - 1)
        return 2 ** (height - 1) + self.get_nodes_count2(root, height, 0, 2 ** (height - 1) - 1)

    # def countNodes(self, root: TreeNode) -> int:
    #     height = self.get_height(root)
    #     if height == 0:
    #         return 0
    #     left = 0
    #     right = 2 ** (height - 1) - 1
    #     node = root
    #     while left < right:
    #         mid = (left + right) // 2 + 1
    #         # if self.check_node_exist(root, 0, 2 ** (height - 1) - 1, mid):
    #         if self.check_node_exist(root, height, mid):
    #             left = mid
    #         else:
    #             right = mid - 1
    #     return 2 ** (height - 1) + left

    def get_height(self, root: TreeNode) -> int: # 0-indexed
        height = 0
        node = root
        while node:
            node = node.left
            height += 1
        return height

    # def check_node_exist(self, node: TreeNode, left: int, right: int, index: int) -> bool:
    #     if left == right:
    #         return not (node is None)
    #     mid = (left + right) // 2 + 1
    #     if index >= mid:
    #         left = mid
    #         node = node.right
    #     else:
    #         right = mid - 1
    #         node = node.left
    #     return self.check_node_exist(node, left, right, index)
        
    def check_node_exist(self, node: TreeNode, height: int, index: int) -> bool:
        left = 0
        right = 2 ** (height - 1) - 1
        for _ in range(height - 1):
            mid = (left + right) // 2 + 1
            if index >= mid:
                left = mid
                node = node.right
            else:
                right = mid - 1
                node = node.left
        
        return node is not None

    def check_node_exist2(self, node: TreeNode, height: int, left: int, right: int, index: int) -> bool:
        for _ in range(height - 1):
            mid = (left + right) // 2
            if index > mid:
                left = mid + 1
                node = node.right
            else:
                right = mid
                node = node.left
        
        return node is not None

    def get_nodes_count(self, node: TreeNode, height: int, left: int, right: int ) -> int:
        if left == right:
            return 2 ** (height - 1) + left
        mid = (left + right) // 2 + 1
        if self.check_node_exist(node, height, mid):
            left = mid
        else:
            right = mid - 1
        return self.get_nodes_count(node, height, left, right)

    def get_nodes_count2(self, node: TreeNode, height: int, left: int, right: int ) -> int:
        if left == right:
            if self.check_node_exist2(node, height, left, right, right):
                return left
            return max(left - 1, 0)
        mid = (left + right) // 2
        if self.check_node_exist2(node, height, left, right, mid):
            left = mid + 1
            node = node.right
        else:
            right = mid
            node = node.left
        height -= 1
        return self.get_nodes_count2(node, height, left, right)