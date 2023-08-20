# # solution 1: bfs
# # T: O(MN), S: O(min(M, N) + 1)
# from collections import deque
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
#         # directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
#         count = 0
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == "1":
#                     count += 1
#                     grid[r][c] = "0"
#                     queue = deque([[r, c]])
#                     while queue:
#                         coordinates = queue.popleft()
#                         for direction in directions:
#                             next_row = coordinates[0] + direction[0]
#                             next_col = coordinates[1] + direction[1]
#                             if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] == "1":
#                                 grid[next_row][next_col] = "0"
#                                 queue.append([next_row, next_col])
        
#         return count

# solution 2: dfs
# T: O(M*N), S: O(M*N) 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    self.dfs(grid, directions, row, col)
        
        return count
    
    def dfs(self, grid, directions, row, col):
        grid[row][col] == "0"
        for direction in directions:
            next_row = row + direction[0]
            next_col = col + direction[1]
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] == "1":
                grid[next_row][next_col] = "0"
                self.dfs(grid, directions, next_row, next_col)
        