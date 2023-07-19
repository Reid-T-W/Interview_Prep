#!/bin/python3

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if list1 is None and list2 is None:
            return list1
        if list1 and list2 is None:
            return list1
        if list2 and list1 is None:
            return list2
        
        # Determine where dummy and cur should initially point to
        # They must point to the smaller value
        if list1.val < list2.val:
            dummy = cur = list1
            list1 = list1.next
        else:
            dummy = cur = list2
            list2 = list2.next


        # iteratively merging the two linked lists
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        # Handling remaining elements in list 1 or 2
        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy


# Examples
sol = Solution()
# list1 = [0,2,5, 6]
# list2 = [1,3,4]
# list1 = [1,2,4]
# list2 = [1,3,4]
# list1 = [2]
# list2 = [1]
# list1 = [1]
# list2 = [2]
list1 = [1]
list2 = [1]
# Create Linked list
def createLinkedList(list):
    node = ListNode()
    node.val = list[0]
    prev = node
    start = node
    for item in list[1:]:
        node = ListNode()
        node.val = item
        prev.next = node
        prev = node
    
    node.next = None
    return start

def printLinkedList(linkedList):
    while linkedList:
        print(linkedList.val)
        linkedList = linkedList.next

linkedList1 = createLinkedList(list1)
linkedList2 = createLinkedList(list2)
printLinkedList(sol.mergeTwoLists(linkedList1, linkedList2))


            