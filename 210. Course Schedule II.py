# Medium — Graph
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# - For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Input: numCourses = 2, prerequisites = 1,0
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

from typing import List

# O(V + E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(graph, node):
            if node in cycle:  
                return False
            if node in seen: 
                return True

            cycle.add(node)
            for neighbor in graph[node]:
                if not dfs(graph, neighbor):
                    return False

            cycle.remove(node)
            seen.add(node)
            output.append(node)

            return True

        def edgelist_adjencylist(numCourses, prerequisites):
            graph = {i: [] for i in range(numCourses)}
            for edge in prerequisites:
                nodeA, nodeB = edge
                graph[nodeA].append(nodeB)
            return graph

        graph = edgelist_adjencylist(numCourses, prerequisites)

        seen = set()
        cycle = set()
        output = []

        for node in range(numCourses):
            if not dfs(graph, node):
                return []

        return output

