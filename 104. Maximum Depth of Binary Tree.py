# recursion
# T: O(N), S: O(logN)->O(N)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # """
        # :type root: TreeNode
        # :rtype: int
        # """ 
        # if root is None: 
        #     return 0 
        # else: 
        #     left_height = self.maxDepth(root.left) 
        #     right_height = self.maxDepth(root.right) 
        #     return max(left_height, right_height) + 1 
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0