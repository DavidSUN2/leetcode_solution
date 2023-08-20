# T: O(N), S: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer approach
        left = 0
        right = len(height) - 1
        most_water = 0
        while left < right:
            most_water = max(most_water, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return most_water