# solution 1: bfs
# T: O(M*N), S: O(M*N)
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        WALL = -1
        GATE = 0
        INF = 2147483647
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        level = 0
        queue = deque()
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == GATE:
                    queue.append([row, col])
        
        while queue:
            current_level = len(queue)
            level += 1
            for _ in range(current_level):
                room = queue.popleft()
                for direction in directions:
                    row_adj = room[0] + direction[0]
                    col_adj = room[1] + direction[1]
                    if 0 <= row_adj < len(rooms) and 0 <= col_adj < len(rooms[0]) and rooms[row_adj][col_adj] == INF:
                        rooms[row_adj][col_adj] = level
                        queue.append([row_adj, col_adj])

                        