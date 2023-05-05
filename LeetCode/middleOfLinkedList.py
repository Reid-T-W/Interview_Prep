from typing import Optional
import math

from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Fast and slow pointer approach
        if head.next == None:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        # if head.next == None:
        #     return head
        # pointer = head
        # counter = 0
        # find_counter = 0
        # # Count the number of elements in the linked list
        # while (pointer.next) != None:
        #     counter += 1
        #     pointer = pointer.next
        # # Get the middle index
        # if counter%2 != 0:
        #     mid = counter//2 + 1
        # else:
        #     mid = counter//2

        # # Retrieve the middle index
        # pointer = head
        
        # while (find_counter != mid):
        #     find_counter += 1
        #     pointer = pointer.next
        # return pointer
    
first = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)


first.next = second
second.next = third
third.next = fourth
fourth.next = None

sol = Solution()
print(sol.middleNode(first).val)