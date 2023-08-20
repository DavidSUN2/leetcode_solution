# # solution 1: bubble sort, time limit exceeded
# # T: O(N^2), S: O(1)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         if len(nums) == 1:
#             return nums[0]

#         count = 1
#         for i in range(len(nums) - 1, 0, -1):
#             for j in range(1, i + 1):
#                 if nums[j] < nums[j - 1]:
#                     nums[j], nums[j - 1] = nums[j - 1], nums[j]
#             if count == k:
#                 return nums[-k]
#             count += 1

#         if k == len(nums):
#             return nums[0]

# # solution 2: quick select1
# # T: O(N^2), S: O(N)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)
        
#     def quick_select(self, nums, left, right, k): # right: inclusive
#         def swap(nums, l, r):
#           temp = nums[l]
#           nums[l] = nums[r]
#           nums[r] = temp

#         partition = left
#         pivot = right
#         for curr in range(left, right):
#             if nums[curr] <= nums[pivot]:
#                 swap(nums, curr, partition)
#                 partition += 1

#         swap(nums, pivot, partition)

#         if partition == k:
#             return nums[partition]
#         elif k < partition:
#             return self.quick_select(nums, left, partition - 1, k)
#         else:
#             return self.quick_select(nums, partition + 1, right, k)


# # solution 3: quick select2
# # T: O(N^2), S: O(N)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#       indexToFind = len(nums) - k
#       return self.quickSelect(nums, 0, len(nums) - 1, indexToFind);

#     def swap(self, nums: list[int], i: int, j: int) -> None:
#       temp = nums[i]
#       nums[i] = nums[j]
#       nums[j] = temp
    
#     def getPartition(self, nums: list[int], left: int, right: int) -> int:
#       i = left
#       for j in range(left, right + 1):
#         if nums[j] <= nums[right]:
#           self.swap(nums, i, j)
#           i += 1
#       return i - 1

#     def quickSelect(self, nums: list[int], left: int, right: int, indexToFind: int) -> int:
#       partitionIndex = self.getPartition(nums, left, right)
#       if partitionIndex == indexToFind:
#         return nums[partitionIndex]
#       elif indexToFind < partitionIndex:
#         return self.quickSelect(nums, left, partitionIndex - 1, indexToFind)
#       else:
#         return self.quickSelect(nums, partitionIndex + 1, right, indexToFind)

# # solution 4
# # T: O(NlogN), S: O(N)
# class Solution:
#     def findKthLargest(self, nums, k):
#         nums.sort(reverse=True)
#         return nums[k - 1]

# # solution 5
# # heapq: min heap
# # T: O(Nlogk), S: O(k)
# class Solution:
#     def findKthLargest(self, nums, k):
#         heap = []
#         for num in nums:
#             heapq.heappush(heap, num)
#             if len(heap) > k:
#                 heapq.heappop(heap)
        
#         return heap[0]

# # solution 6: quick select 3
# # T: O(N^2), S: O(N)
# class Solution:
#     def findKthLargest(self, nums, k):
#         def quick_select(nums, k):
#             pivot = random.choice(nums)
#             left, mid, right = [], [], []

#             for num in nums:
#                 if num > pivot:
#                     left.append(num)
#                 elif num < pivot:
#                     right.append(num)
#                 else:
#                     mid.append(num)
            
#             if k <= len(left):
#                 return quick_select(left, k)
            
#             if len(left) + len(mid) < k:
#                 return quick_select(right, k - len(left) - len(mid))
            
#             return pivot
        
#         return quick_select(nums, k)

# solution 7: quick select4
# T: O(N^2), S: O(N)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)
        
    def quick_select(self, nums, left, right, k): # right: inclusive
        def swap(nums, l, r):
          temp = nums[l]
          nums[l] = nums[r]
          nums[r] = temp

        cross = False
        pivot = random.choice(range(left, right + 1))
        partition = left

        for curr in range(left, right + 1):
            if partition == pivot and partition < right:
                partition += 1
                cross = True
            if curr != pivot and nums[curr] <= nums[pivot]:
                swap(nums, curr, partition)
                partition += 1
            
        partition = partition - 1 if cross == True else partition
        swap(nums, pivot, partition)

        if partition == k:
            return nums[partition]
        elif k < partition:
            return self.quick_select(nums, left, partition - 1, k)
        else:
            return self.quick_select(nums, partition + 1, right, k)