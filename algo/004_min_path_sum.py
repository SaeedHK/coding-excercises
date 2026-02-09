"""
64. Minimum Path Sum (Leetcode)
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
"""

from abc import update_abstractmethods
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mapping: dict = {}
        discovered = set()

        n = len(grid)
        m = len(grid[0])
        mapping[f"{n - 1},{m - 1}"] = grid[n - 1][m - 1]
        discovered.add(f"{n - 1},{m - 1}")

        def get_neighbors(i, j):
            neigthbors = [
                f"{k},{l}"
                for k in [i + 1, i]
                for l in [j + 1, j]
                if k < n and l < m and abs(k - i) + abs(l - j) == 1
            ]
            # print(f"update {i},{j} with neightbors {neigthbors}")
            return neigthbors

        def update(i, j):
            neigthbors = get_neighbors(i, j)
            if not all(neightbor in discovered for neightbor in neigthbors):
                return

            mapping[f"{i},{j}"] = (
                min((mapping[neightbor] for neightbor in neigthbors)) + grid[i][j]
            )
            discovered.add(f"{i},{j}")

        for s in range(m + n - 3, -1, -1):
            print(f"update with sum {s}")
            for k in range(max(s - m + 1, 0), n):
                update(k, s - k)

        return mapping["0,0"]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
assert Solution().minPathSum(grid) == 7
print("All test cases passed")
