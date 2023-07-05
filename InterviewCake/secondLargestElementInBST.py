#!/bin/python3

import unittest

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left
    
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
    

def find_second_largest(root_node):
    temp = root_node
    prev = None
    largest = None

    # Edge case where the root node does not have a left and right child
    if not temp.left and not temp.right:
        raise Exception('Needed a minimum of two nodes in the tree')
    

    # Find the largest element
    if not temp.right:
        largest = temp
    else:
        while temp.right:
            prev = temp
            temp = temp.right
        largest = temp

    # Find the second largest element

    # Handles the case where the largest node does not
    # have a left child, this is valid if the largest
    # node is not root (meaning the prev value will not be none)
    if not largest.left and prev:
        return prev.value
    
    # Handles the case where the largest node has a left child
    second_largest = largest.left
    if second_largest.right:
        while second_largest.right:
            second_largest = second_largest.right
    return second_largest.value
    


    
    


# def find_second_largest(root_node):
#     LEFT_TURN = False
#     prev = curr = None
#     temp = root_node
#     if not temp.right:
#         #if temp.left:
#         #    prev = temp.left
#         pass
#         # return temp.left
#     else:
#         while temp:
#             if not LEFT_TURN:
#                 prev = curr
#                 curr = temp
#             else:
#                 prev = temp
#             if not temp.right and temp.left:
#                 curr = temp
#                 temp = temp.left
#                 LEFT_TURN = True
#             else:
#                 temp = temp.right
            
#     return prev.value
    # raise Exception('Needed a minimum of two nodes in the tree')

# BinaryTreeNode = BinaryTreeNode
# def test_largest_has_a_left_child():
#     tree = BinaryTreeNode(50)
#     left = tree.insert_left(30)
#     right = tree.insert_right(70)
#     left.insert_left(10)
#     left.insert_right(40)
#     right.insert_left(60)
#     actual = find_second_largest(tree)
#     expected = 60
#     # self.assertEqual(actual, expected)
#     print(actual)

# test_largest_has_a_left_child()

# Tests

class Test(unittest.TestCase):

    BinaryTreeNode = BinaryTreeNode
    
    def test_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        actual = find_second_largest(tree)
        expected = 70
        self.assertEqual(actual, expected)

    def test_largest_has_a_left_child(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        actual = find_second_largest(tree)
        expected = 60
        self.assertEqual(actual, expected)

    def test_largest_has_a_left_subtree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right_left = right.insert_left(60)
        right_left_left = right_left.insert_left(55)
        right_left.insert_right(65)
        right_left_left.insert_right(58)
        actual = find_second_largest(tree)
        expected = 65
        self.assertEqual(actual, expected)

    def test_second_largest_is_root_node(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        actual = find_second_largest(tree)
        expected = 50
        self.assertEqual(actual, expected)

    def test_two_nodes_root_is_largest(self):
        tree = Test.BinaryTreeNode(50)
        tree.insert_left(30)
        actual = find_second_largest(tree)
        expected = 30
        self.assertEqual(actual, expected)

    def test_second_largest_right_offshoot_left(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        left.insert_right(40)
        left.insert_left(10)
        actual = find_second_largest(tree)
        expected = 40
        self.assertEqual(actual, expected)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        actual = find_second_largest(tree)
        expected = 40
        self.assertEqual(actual, expected)

    def test_ascending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(60)
        right_right = right.insert_right(70)
        right_right.insert_right(80)
        actual = find_second_largest(tree)
        expected = 70
        self.assertEqual(actual, expected)

    def test_error_when_tree_has_one_node(self):
        tree = Test.BinaryTreeNode(50)
        with self.assertRaises(Exception):
           find_second_largest(tree)

    def test_error_when_tree_is_empty(self):
        with self.assertRaises(Exception):
           find_second_largest(None)


unittest.main(verbosity=2)
