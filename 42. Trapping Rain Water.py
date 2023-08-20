# T: O(N), S: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0:
            return 0
            
        trapped_water = 0
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[-1]

        while left <= right:

            if left_max < right_max:
                left_max = max(left_max, height[left])
                trapped_water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                trapped_water += right_max - height[right]
                right -= 1
        return trapped_water
