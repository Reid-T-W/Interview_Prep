from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if (not head or not head.next):
            return False
        fast = head.next
        while fast != None and fast.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


# [3,2,0,-4] p=1

first = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

first.next = second
second.next = third
third.next = fourth
fourth.next = second

sol = Solution()
print(sol.hasCycle(first))