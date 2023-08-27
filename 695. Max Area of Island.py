# Medium — Graph 
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 9

from typing import List

# O(n * m)
class Solution: 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()

        def dfs(grid, row, col, count):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                return 0
            
            if grid[row][col] == 0:
                return 0

            if (row, col) in seen:
                return 0

            seen.add((row, col))

            count = 1

            count += dfs(grid, row + 1, col, count)
            count += dfs(grid, row - 1, col, count)
            count += dfs(grid, row, col + 1, count)
            count += dfs(grid, row, col - 1, count)

            return count

        area = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                area = max(area, dfs(grid, row, col, 0))
        
        return area


