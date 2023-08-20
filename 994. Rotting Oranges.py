# solution 1: bfs
# T: O(M*N), S: O(M*N)
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        minute = 0
        queue = deque()
        count_fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == ROTTEN:
                    queue.append([row, col])
                if grid[row][col] == FRESH:
                    count_fresh += 1
        
        while queue:
            current_rotten = len(queue)
            have_fresh_adj = False
            for _ in range(current_rotten):
                rotten_orange = queue.popleft()
                for direction in directions:
                    row_adj = rotten_orange[0] + direction[0]
                    col_adj = rotten_orange[1] + direction[1]
                    if 0 <= row_adj < len(grid) and 0 <= col_adj < len(grid[0]) and grid[row_adj][col_adj] == FRESH:
                        have_fresh_adj = True
                        grid[row_adj][col_adj] = ROTTEN
                        count_fresh -= 1
                        queue.append([row_adj, col_adj])
            if have_fresh_adj == True:
                minute += 1
        
        return minute if count_fresh == 0 else -1



# DFS should not work easily