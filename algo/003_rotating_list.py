"""
61. Rotate List (Leetcode)
Given the head of a linked list, rotate the list to the right by k places.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, lst):
        head = None
        current = None
        for val in lst:
            if not head:
                head = cls(val, None)
                current = head
            else:
                current.next = ListNode(val, None)
                current = current.next

        return head

    def to_list(self):
        lst = []
        head = self
        while head:
            lst.append(head.val)
            head = head.next

        return lst


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if k <= 0:
            return head

        start, end = self.find_start_end(head, k)

        if start is None:
            return head

        end.next = head
        final_array = start.next
        start.next = None

        return final_array

    def find_start_end(self, head: ListNode, k: int, length: Optional[int] = None):
        if length and k >= length:
            k = k % length

        if k <= 0:
            return None, None

        start, end = head, head
        diff = 0

        while end.next is not None:
            end = end.next
            if diff == k:
                start = start.next
            else:
                diff += 1

        if diff >= k:
            return start, end

        return self.find_start_end(head, k - diff - 1, diff + 1)


list_node = Solution().rotateRight(ListNode.from_list([1, 2, 3, 4, 5]), 3)
assert list_node and list_node.to_list() == [3, 4, 5, 1, 2]

list_node = Solution().rotateRight(ListNode.from_list([0, 1, 2]), 4)
assert list_node and list_node.to_list() == [2, 0, 1]

print("All tests passed!")
