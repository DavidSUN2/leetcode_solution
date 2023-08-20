# T: O(N), S: O(N)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_list = list(s)
        for c in range(len(s_list)):
            if s_list[c] == "(":
                stack.append(c)
            elif s_list[c] == ")":
                if stack:
                    stack.pop()
                else:
                    s_list[c] = ""
        for i in range(len(stack)):
            s_list[stack[i]] = ""

        return "".join(s_list)

        # paren_dict = {'(': [], ')': []}
        # for c in range(len(s)):
        #     if s[c] == '(':
        #         paren_dict[s[c]].append(c)
        #     if s[c] == ')':
        #         if len(paren_dict['(']) > 0:
        #             paren_dict['('].pop()
        #         else:
        #             paren_dict[s[c]].append(c)

        # s_new = ''.join([s[i] for i in range(len(s)) if i not in paren_dict['('] + paren_dict[')']])
        # return s_new