# T: O(N), S: O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ps = len(s) - 1
        pt = len(t) - 1
        while ps >= 0 or pt >= 0:
            cs, ps = self.get_current_character(s, ps)
            ct, pt = self.get_current_character(t, pt)
            if cs != ct:
                return False
        return True

    def get_current_character(self, string: str, position: int) -> Tuple[str, int]:
        if position == -1:
            return '', -1

        if string[position] != '#':
            return string[position], position - 1
        else:
            skip = 1
        
        while skip >= 0:
            position -= 1
            if position == -1:
                return '', -1
            if string[position] == '#':
                skip += 1
            elif string[position] != '#' and skip > 0:
                skip -= 1
            else:
                return string[position], position - 1