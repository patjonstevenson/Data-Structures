import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Value greater than tree value => go right
        if value >= self.value:
            # If no value to the right, create one
            if not self.right:
                self.right = BinarySearchTree(value)
            # Otherwise, move to that level recursively
            else:
                self.right.insert(value)
        # Value less than tree value => go left
        elif value < self.value:
            # If no value to the left, create one
            if not self.left:
                self.left = BinarySearchTree(value)
            # Otherwise, move to that level recursively
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If tree value is our value, we found it, so return True
        if self.value == target:
            return True
        # If tree value is less than our value, look right
        if target > self.value:
            # If no value to the right,
            #  return False b/c tree doesn't contain our value
            if not self.right:
                return False
            # Otherwise, move to the next level recursively
            return self.right.contains(target)
        # If tree value is greater than our value, look left
        elif target < self.value:
            # If no value to the left,
            #  return False b/c tree doesn't contain our value
            if not self.left:
                return False
            # Otherwise, move to the next level recursively
            return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
