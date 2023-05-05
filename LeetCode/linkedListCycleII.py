from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's cycle based approach
        if not head or not head.next:
            return None
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            if slow == fast:
                new_slow = head
                while (new_slow != slow):
                    # print(new_slow.val, slow.val)
                    new_slow = new_slow.next
                    slow = slow.next
                return new_slow
            slow = slow.next
            fast = fast.next.next
        return None
    
        # # Set based approch
        # counter = 0
        # traversed = dict()
        # pointer = head
        # while pointer not in traversed:
        #     if (not pointer.next):
        #         return None
        #     traversed[pointer] = counter
        #     pointer = pointer.next
        #     counter += 1
        # return pointer


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
print(sol.hasCycle(first).val)