# # solution 1: brute force
# # Time limit exceeded
# # T: O(N^2), S: O(N)
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         for i in range(len(s) - 1 ):
#             s_new = s[0:i] + s[i + 1:]
#             if self.is_palindrome(s_new):
#                 return True
#         if self.is_palindrome(s[0:-1]):
#             return True
#         return False


#     def is_palindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True

# # solution 2
# # T: O(N), S: O(1)
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             if s[left] != s[right]:
#                 break
#             left += 1
#             right -= 1
#         if left >= right:
#             return True

#         left_new = left + 1
#         right_new = right - 1
#         while left_new < right:
#             if s[left_new] != s[right]:
#                 break
#             left_new += 1
#             right -= 1
#         if left_new >= right:
#             return True
        
#         while left < right_new:
#             if s[left] != s[right_new]:
#                 break
#             left += 1
#             right_new -= 1
#         if left >= right_new:
#             return True
        
#         return False
        
# # solution 3
# # T: O(N), S: O(1)
# class Solution:
#     def validPalindrome(self, s: str) -> bool:

#         check, left, right = self.is_palindrome(s, 0, len(s) - 1)
#         if check:
#             return True
#         left_new = left + 1
#         right_new = right - 1
#         return self.is_palindrome(s, left_new, right)[0] or self.is_palindrome(s, left, right_new)[0]

#     def is_palindrome(self, s: str, left: int, right: int) -> bool:
#         while left < right:
#             if s[left] != s[right]:
#                 return False, left, right
#             left += 1
#             right -= 1
#         return True, left, right
        
# solution 4
# T: O(N), S: O(1) 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.valid_sub_palindrome(s, left + 1, right) or self.valid_sub_palindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True

    def valid_sub_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True