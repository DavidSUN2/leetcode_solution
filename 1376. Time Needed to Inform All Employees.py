# # solution: bfs
# # T: O(N), S: O(N)
# from collections import deque
# class Solution:
#     def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#         if n == 1:
#             return 0
#         adjacency_list = {}
#         finalTime = [0 for i in range(n)]
#         for i in range(len(manager)):
#             if i != -1:
#                 if manager[i] not in adjacency_list:
#                     adjacency_list[manager[i]] = []
#                 adjacency_list[manager[i]].append(i)
#         queue = deque([headID])
#         finalTime[headID] = 0
#         while queue:
#             manager_id = queue.popleft()
#             for subordinate_id in adjacency_list[manager_id]:
#                 finalTime[subordinate_id] = informTime[manager_id] + finalTime[manager_id]
#                 if len(adjacency_list.get(subordinate_id, [])) > 0:
#                     queue.append(subordinate_id)

#         return max(finalTime)

# # solution 2: DFS
# # T: O(N), S: O(N)

# class Solution:
#     def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#         adjacency_list = {}
#         for i in range(n):
#             if i != -1:
#                 adjacency_list[manager[i]] = adjacency_list.get(manager[i], []) + [i]

#         finalTime = [0 for i in range(n)]
#         self.dfs(headID, adjacency_list, informTime, finalTime)
#         return max(finalTime)  
             
#     def dfs(self, manager_id: int, adjacency_list: dict[list[int]], informTime: list[int], finalTime: list[int]) -> None:
#         for subordinate_id in adjacency_list.get(manager_id, []):
#             finalTime[subordinate_id] = finalTime[manager_id] + informTime[manager_id]
#             self.dfs(subordinate_id, adjacency_list, informTime, finalTime)

# # solution 3: DFS without finalTime
# # T: O(N), S: O(N)

# class Solution:
#     def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#         adjacency_list = defaultdict(list)
#         for i in range(n):
#             if i != -1:
#                 adjacency_list[manager[i]].append(i)

#         # finalTime = [0 for i in range(n)]
#         return self.dfs(headID, adjacency_list, informTime, 0)
           
#     def dfs(self, manager_id: int, adjacency_list: dict[list[int]], informTime: list[int], manager_time: int) -> int:
#         max_time = 0
#         for subordinate_id in adjacency_list.get(manager_id, []):
#             subordinate_time = informTime[manager_id] + manager_time
#             max_time = max(max_time, subordinate_time, self.dfs(subordinate_id, adjacency_list, informTime, subordinate_time))
#         return max_time

# solution 4: DFS without finalTime
# T: O(N), S: O(N)

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacency_list = defaultdict(list)
        for i in range(n):
            if i != -1:
                adjacency_list[manager[i]].append(i)
        return self.dfs(headID, adjacency_list, informTime)
           
    def dfs(self, manager_id: int, adjacency_list: dict[list[int]], informTime: list[int]) -> int:
        max_time = 0
        for subordinate_id in adjacency_list[manager_id]:
            max_time = max(max_time, self.dfs(subordinate_id, adjacency_list, informTime))
        return max_time + informTime[manager_id]