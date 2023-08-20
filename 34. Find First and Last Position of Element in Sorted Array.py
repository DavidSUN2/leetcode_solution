# # solution 1: recursion
# # T: O(logn) S: O(logn)
# class Solution:
#     def searchRange(self, nums: list[int], target: int) -> list[int]:
#         return self.findBound(nums, target, 0, len(nums) - 1)

#     def findBound(self, nums: list[int], target: int, left: int, right: int) -> None:
#         if left > right:
#             return [-1, -1]

#         median = (right + left) // 2

#         if nums[median] == target:
#             begin = self.findBegin(nums, target, left, median)
#             end = self.findEnd(nums, target, median, right)
#         elif nums[median] < target:
#             return self.findBound(nums, target, median + 1, right)
#         else:
#             return self.findBound(nums, target, left, median - 1)

#         return [begin, end]

#     def findBegin(self, nums: list[int], target: int, left: int, median: int) -> int:
#         if (median - 1 >= 0 and nums[median - 1] != target) or (median == 0):
#             return median
#         mid = (median + left) // 2
#         if nums[mid] == target:
#             return self.findBegin(nums, target, left, mid)
#         return self.findBegin(nums, target, mid + 1, median)

#     def findEnd(self, nums: list[int], target: int, median: int, right: int) -> int:
#         if (median + 1 < len(nums) and nums[median + 1] != target) or (median == len(nums) - 1):
#             return median
#         mid = (median + right) // 2 + 1
#         if nums[mid] == target:
#             return self.findEnd(nums, target, mid, right)
#         return self. findEnd(nums, target, median, mid - 1)

# solution 2: iteration
# T: O(logn), S: O(1)
class Solution:       
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                break
        
        if left > right:
            return [-1, -1]

        left_start = left
        right_start = mid
        left_end = mid
        right_end = right

        while left_start <= right_start:
            mid_start = (left_start + right_start) // 2
            if nums[mid_start] < target:
                left_start = mid_start + 1
            else:
                right_start = mid_start - 1
        if nums[mid_start] < target:
            start = mid_start + 1
        else:
            start = mid_start

        while left_end <= right_end:
            mid_end = (left_end + right_end) // 2
            if nums[mid_end] > target:
                right_end = mid_end - 1
            else:
                left_end = mid_end + 1
        if nums[mid_end] > target:
            end = mid_end - 1
        else:
            end = mid_end

        return [start, end]
        