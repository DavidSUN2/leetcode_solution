# # solution 1: iterative dfs
# # T: O(N!?), S: O(E+N)
# from collections import defaultdict
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         adj_list = defaultdict(list)
#         for src, tgt, edge_time in times:
#             adj_list[src].append([tgt, edge_time])
#         visited = defaultdict(int) # BE CAREFUL ABOUT INT OR LIST INSIDE DICT
#         # visited[k] = 0   # THIS LINE CAUSED WRONG ANS
#         stack = [(k, 0)] # here the time is latest total time

#         while stack:
#             node, time = stack.pop()
#             if node not in visited or visited[node] > time:
#                 visited[node] = time
#                 if node in adj_list:
#                     for next_node, edge_time in adj_list[node]:
#                         stack.append((next_node, time + edge_time))
                
#         if len(visited) < n:
#             return -1
        
#         return max(visited.values())

# solution 2: recursive dfs
# T: O((N-1)!?), S: O(E+N)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for src, tgt, edge in times:
            adj_list[src].append((tgt, edge))
        for node in adj_list:  # this can increase speed a lot
            adj_list[node].sort(key = lambda x: x[1])

        visited = defaultdict(int)
        self._dfs(k, adj_list, visited, 0)
        if len(visited) < n:
            return -1
        return max(visited.values())
    
    def _dfs(self, node: int, adj_list: dict[list[int]], visited: dict[int], time: int) -> None:    
        if node not in visited or visited[node] > time:
            visited[node] = time
            if node in adj_list:
                for next_node, edge in adj_list[node]:
                    self._dfs(next_node, adj_list, visited, time + edge)

# # solution 3: Dijkstra's algorithm
# # T: O(ElogN +NlogN), S: O(E+N)
# from collections import defaultdict
# import heapq
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         adj_list = defaultdict(list)
#         for src, tgt, edge_time in times:
#             adj_list[src].append([tgt, edge_time])
#         visited = defaultdict(int) # BE CAREFUL ABOUT INT OR LIST INSIDE DICT
#         # visited[k] = 0   # THIS LINE CAUSED WRONG ANS
        
#         heap = []
#         heapq.heappush(heap, (0, k))  # Dijkstra: just change stack to heap

#         while heap:
#             time, node = heapq.heappop(heap)
#             if node not in visited or visited[node] > time:
#                 visited[node] = time
#                 if node in adj_list:
#                     for next_node, edge_time in adj_list[node]:
#                         heapq.heappush(heap, (time + edge_time, next_node))
                
#         if len(visited) < n:
#             return -1
        
#         return max(visited.values())