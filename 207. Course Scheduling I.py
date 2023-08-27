# Medium — Graph
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you **must** take course bi first if you want to take course ai.
# - For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Input: numCourses = 2, prerequisites = 1,
# Output: true
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

from typing import List

# O(V + E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(graph, node):
            if node in seen:
                return False
            if node in done:
                return True
            
            seen.add(node)

            for neighbor in graph[node]:
                if not dfs(graph, neighbor):
                    return False
            
            seen.remove(node)
            done.remove(node)

            return True

        def edgelist_adjencylist(numCourses, prerequisites):
            graph = {i: [] for i in range(numCourses)}
            
            for edge in prerequisites:
                nodeA, nodeB = edge
                graph[nodeA].append(nodeB)
                
            return graph


        graph = edgelist_adjencylist(numCourses, prerequisites)

        seen = set()
        done = set()

        for node in range(numCourses):
            if not dfs(graph, node):
                return False
        
        return True
