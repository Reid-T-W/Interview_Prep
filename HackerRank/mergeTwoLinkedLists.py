#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    """
    Given two linked lists it merges them in a sorted manner
    Returns:
        A sorted linked list
    """
    mergedList = None
    # If both list are empty return an empty list
    if not head1 and not head2:
        return head1
    
    # mergedList = SinglyLinkedListNode()
    # If list one is empty return list two
    if not head1:
        mergedList = head2
        return mergedList

    # If list two is empty return list one
    if not head2:
        mergedList = head1
        return mergedList
    
    # Compare the values in each of the heads and find the one with
    # the lowest value, keep on incrementing to the next node until
    # you find a value greater than the value in the other list
    if head1.data <= head2.data: 
        mergedList = head1
        while (head1 and head1.data <= head2.data):
            prev1 = head1
            head1 = head1.next
        # temp = prev1
        prev1.next = head2
        # Iterate to the end of head 2 to get the last Node and connect
        # with list 1
        while head2.next is not None:
            head2 = head2.next
        head2.next = head1
        return mergedList
    
    if head2.data <= head1.data:
        mergedList = head2
        while (head2 and head2.data <= head1.data):
            prev2 = head2
            head2 = head2.next
        prev2.next = head1
        # Iterate to the end of head 1 to get the last Node and connect
        # with list 2
        while head1.next is not None:
            head1 = head1.next
        head1.next = head2
        return mergedList
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
