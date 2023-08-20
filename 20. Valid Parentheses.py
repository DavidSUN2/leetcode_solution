# T: O(N), S: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        map = {']': '[', '}': '{', ')': '('}
        stack = []
        for c in s:
            if c not in map:
                stack.append(c)
            else:
                last_char = stack.pop() if stack else '#'
                if last_char != map[c]:
                    return False

        return not stack

        # char_stack = []
        # for c in s:
        #     if c == "(":
        #         char_stack.append('(')
        #     elif c == "{":
        #         char_stack.append('{')
        #     elif c == "[":
        #         char_stack.append('[')
        #     elif c == ")":
        #         if len(char_stack) == 0:
        #             return False
        #         last_char = char_stack.pop()
        #         if last_char != "(":
        #             return False               
        #     elif c == "}":
        #         if len(char_stack) == 0:
        #             return False
        #         last_char = char_stack.pop()
        #         if last_char != "{":
        #             return False
        #     elif c == "]":
        #         if len(char_stack) == 0:
        #             return False
        #         last_char = char_stack.pop()
        #         if last_char != "[":
        #             return False
        
        # if len(char_stack) > 0:
        #     return False

        # return True