"""
86. Partition List (LeetCode)
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = None
        start_left = None

        right = None
        start_right = None

        while head:
            val = head.val
            if val < x:
                if not left:
                    left = ListNode(val, None)
                    start_left = left
                else:
                    left.next = ListNode(val, None)
                    left = left.next

            else:
                if not right:
                    right = ListNode(val, None)
                    start_right = right
                else:
                    right.next = ListNode(val, None)
                    right = right.next

            head = head.next

        if start_left and start_right:
            if not left:
                raise Exception(
                    "Unexpected state: left is None but start_left is not None"
                )

            left.next = start_right
            return start_left
        if not start_left:
            return start_right
        if not start_right:
            return start_left


list_node = Solution().partition(ListNode.from_list([1, 4, 3, 2, 5, 2]), 3)
assert list_node and list_node.to_list() == [1, 2, 2, 4, 3, 5]
print("All tests passed!")
