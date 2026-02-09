"""
64. Minimum Path Sum (Leetcode)
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mapping = {
            f"{i},{j}": False for i in range(len(grid)) for j in range(len(grid[0]))
        }

        n = len(grid)
        m = len(grid[0])

        if n == 1:
            mapping[f"{i},{j}"] = grid[0][:k]

        discovered = set()

        return 0


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
assert Solution().minPathSum(grid) == 7
