from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Setup a stack, to store new elements and pop
        # recurring elements as we go
        stack = []
        if head == None or head.next == None:
            return True
        stack.append(head.val)
        while head.next != None:
            head = head.next
            if len(stack) == 0:
                stack.append(head.val)
            elif stack[-1] != head.val:
                stack.append(head.val)
            else:
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

first = ListNode(2)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(3)
fifth = ListNode(2)
sixth = ListNode(3)


first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = None

sol = Solution()
print(sol.isPalindrome(first))