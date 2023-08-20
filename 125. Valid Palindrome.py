# T: O(N), S: O(N)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for l in s:
            if l.isalnum():
            # if 'a' <= l.lower() <= 'z' or '0' <= l <= '9':
                s_new += l.lower()
        
        if len(s_new) == 1:
            return True

        left = 0
        right = len(s_new) - 1
        while left < right:
            if s_new[left] != s_new[right]:
                return False
            left += 1
            right -= 1
        
        return True