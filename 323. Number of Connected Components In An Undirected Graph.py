# Medium — Graph
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [a_i, b_i] indicates that there is an edge between a_i and b_i in the graph. 
# Return the number of connected components in the graph

# Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
# Output: 2

from typing import List, Dict

# O(E + V)
class Solution:
    def edge_list_to_adjcency_list(self, edges: List[List[int]]) -> Dict[int, List[int]]:
        output_graph = {}

        for edge in edges:
            node1, node2 = edge
            if node1 not in output_graph:
                output_graph[node1] = []
            if node2 not in output_graph:
                output_graph[node2] = []

            output_graph[node1].append(node2)
            output_graph[node2].append(node1)

        return output_graph

    def connected_components(self, edges: List[List[int]]) -> int:
        # Convert edges to adjacency list
        graph = self.edge_list_to_adjcency_list(edges)
    
        # Initialize visited nodes set
        seen = set()

        # Initialize count of connected components
        count = 0

        def dfs(graph, node):
            # Mark the node as visited
            seen.add(node)
            
            # Visit all the neighbors
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(graph, neighbor)

            # Perform DFS on each node
            for node in graph:
                if node not in seen:
                    dfs(graph, node)
                    count += 1

            return count