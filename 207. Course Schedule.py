# # solution: bfs, don't work
# # T: O(N), S: O(N)
# from collections import deque
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         visited = [0 for i in range(numCourses)]
#         queue = deque()
#         course_have_pre = defaultdict(int)
#         adj_list = defaultdict(list)
#         for pre in prerequisites:
#             if pre[0] == pre[1]:
#                 return False
#             course_have_pre[pre[0]] += 1
#             adj_list[pre[1]].append(pre[0])
#         for i in range(numCourses):
#             if i not in course_have_pre:
#                 queue.append(i)
#                 visited[i] += 1
#         if len(queue) == 0:
#             return False

#         while queue:
#             current_level = len(queue)
#             for _ in range(current_level):
#                 course = queue.popleft()
                
#                 if course in course_have_pre and visited[course] > course_have_pre[course]:
#                     return False
#                 for c in adj_list[course]:
#                     if visited[c] == 0:
#                         queue.append(c)
#                     visited[c] += 1
#         for c in visited:
#             if c == 0:
#                 return False

#         return True

# # solution 2: dfs, don't work
# # 
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         adj_list = defaultdict(list)
#         course_have_pre = defaultdict(int)
#         course_not_have_pre = []
#         for pre in prerequisites:
#             adj_list[pre[1]].append(pre[0])
#             course_have_pre[pre[0]] += 1
#         for i in range(numCourses):
#             if i not in course_have_pre:
#                 course_not_have_pre.append(i)
#         visited_global = defaultdict(int)
#         for course in course_not_have_pre:
#             visited = defaultdict(int)
#             visited[course] = 1
#             visited_global[course] = 1
#             if self.loop_exist_dfs(adj_list, course_have_pre, course, visited, visited_global):
#                 return False
        
#         for i in range(numCourses):
#             if visited_global[i] == 0:
#                 return False
#         return True

#     def loop_exist_dfs(self, adj_list, course_have_pre, course, visited, visited_global):
#         # if adj_list[course] == []:
#         #     visited = defaultdict(int)
#         for next_course in adj_list[course]:
#             visited[next_course] += 1
#             visited_global[next_course] = 1
#             if visited[next_course] > course_have_pre[next_course]:
#                 return True
#             return self.loop_exist_dfs(adj_list, course_have_pre, next_course, visited, visited_global)
#         # visited[course] = 0
#         return False

# # solution 3: bfs
# # T: O(E+ N**3), S: O(E)
# from collections import defaultdict, deque
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         adj_list = defaultdict(list)
#         for pre in prerequisites:
#             adj_list[pre[1]].append(pre[0])
#         course_pre = list(adj_list)

#         for course in course_pre:
#             visited = {}
#             next_courses = adj_list[course]
#             queue = deque()
#             for next_course in next_courses:
#                 visited[next_course] = True
#                 queue.append(next_course)
#             while queue:
#                 next_course = queue.popleft()
#                 if next_course == course:
#                     return False
#                 for c in adj_list[next_course]:
#                     if c not in visited:
#                         visited[c] = True
#                         queue.append(c)
#         return True

# # solution 4: dfs
# # T: O(E + N**3), S: O(E)
# from collections import defaultdict
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         adj_list = defaultdict(list)
#         for pre in prerequisites:
#             adj_list[pre[1]].append(pre[0])
#         course_pre = list(adj_list)

#         for init_course in course_pre:
#             visited = {}
#             if self.exist_loop_dfs(adj_list, init_course, init_course, visited):
#                 return False
        
#         return True

#     def exist_loop_dfs(self, adj_list: dict[list[int]], init_course: int, curr_course: int, visited: dict) -> bool:
#         for next_course in adj_list[curr_course]:
#             if next_course not in visited:
#                 visited[next_course] = True
#                 if next_course == init_course:
#                     return True
#                 if self.exist_loop_dfs(adj_list, init_course, next_course, visited):
#                     return True
#         return False

# # solution 5: topological sort with adj_list
# # T: O(P+N), S: O(P+N)
# from collections import deque
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         adj_list = defaultdict(list)
#         degrees = defaultdict(int)
#         for pre in prerequisites:
#             adj_list[pre[1]].append(pre[0])
#             degrees[pre[0]] += 1
        
#         queue = deque()
#         for i in range(numCourses):
#             if degrees[i] == 0:
#                 queue.append(i)
        
#         while queue:
#             course = queue.popleft()
#             for adj in adj_list[course]:
#                 if degrees[adj] != 0:
#                     degrees[adj] -= 1
#                     if degrees[adj] == 0:
#                         queue.append(adj)
        
#         for i in range(numCourses):
#             if degrees[i] > 0:
#                 return False
#         return True   

# # solution 6: topological sort without adj_list
# # T: O(P*N), S: O(N)
# from collections import deque
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         degrees = defaultdict(int)
#         for pre in prerequisites:
#             degrees[pre[0]] += 1
        
#         queue = deque()
#         for i in range(numCourses):
#             if degrees[i] == 0:
#                 queue.append(i)
        
#         while queue:
#             course = queue.popleft()
#             for pre in prerequisites:
#                 if pre[1] == course:
#                     if degrees[pre[0]] != 0:
#                         degrees[pre[0]] -= 1
#                         if degrees[pre[0]] == 0:
#                             queue.append(pre[0])
        
#         for i in range(numCourses):
#             if degrees[i] > 0:
#                 return False
#         return True   

# solution 7: dfs recursion
# T: O(P+N), S: O(P+N)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for pre in prerequisites:
            adj_list[pre[1]].append(pre[0])
        
        course_pre = list(adj_list)
        visited = [False] * numCourses
        init_stack = [False] * numCourses

        for i in course_pre:
            if self.cycle_exist_dfs(i, adj_list, visited, init_stack):
                return False
        return True
    
    def cycle_exist_dfs(self, course: int, adj_list: dict[list[int]], visited: list[bool], init_stack: list[bool]) -> bool:
        if init_stack[course]:
            return True
        if visited[course]:
            return False
        
        init_stack[course] = True
        visited[course] = True

        for next_course in adj_list[course]:
            if self.cycle_exist_dfs(next_course, adj_list, visited, init_stack):
                return True
        
        init_stack[course] = False
        return False
        

        