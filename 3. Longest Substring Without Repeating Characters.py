# T: O(N), S: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in [0, 1]:
            return len(s)
        
        char_seen = {}
        global_max = 0
        # local_max = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in char_seen:
                # local_max += 1
                char_seen[s[right]] = right
            else:
                global_max = max(right - left, global_max)
                left = max(left, char_seen[s[right]] + 1)
                # local_max = right - left
                char_seen[s[right]] = right

        return max(global_max, right - left + 1)
                