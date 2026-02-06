"""
79. Word Search (Leetcode)
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        mapping = self.get_mappings(board)
        for char in word:
            if not mapping.get(char, []):
                return False

        cords = self.get_cords(mapping, word)

        return bool(cords)

    def get_mappings(self, board: List[List[str]]) -> dict:
        mapping = {}
        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element not in mapping:
                    mapping[element] = set()
                mapping[element].add(f"{i},{j}")

        return mapping

    def is_adjecent(self, cord_1, cord_2):
        x_1, y_1 = cord_1.split(",")
        x_2, y_2 = cord_2.split(",")

        return (abs(int(x_1) - int(x_2)) + abs(int(y_1) - int(y_2))) < 2

    def get_cords(self, mapping: dict, word: str) -> List[List[int]]:
        if len(word) == 1:
            return [[w] for w in mapping.get(word, [])]

        sub_cords = self.get_cords(mapping, word[1:])
        char = word[0]
        char_cords = mapping.get(char, [])
        new_cords = []
        for cords in sub_cords:
            for c in char_cords:
                if c in cords:
                    continue
                if not self.is_adjecent(c, cords[0]):
                    continue
                new_cords.append([c, *cords])

        return new_cords


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
assert Solution().exist(board, word)
print("Test passed!")
