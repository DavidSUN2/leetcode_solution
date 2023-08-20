class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_dict = {}
        for i in range(len(nums)):
            if nums[i] not in visited_dict:
                visited_dict[target - nums[i]] = i
            else:
                return [visited_dict[nums[i]], i]
        return []
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]