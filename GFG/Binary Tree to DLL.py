#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self,root):
        # do Code here
        start, end = self.demand(root)
        return start

    def demand(self, root):
        if root is None: return None, None
        ll, lr = self.demand(root.left)
        if lr is not None:
            root.left = lr
            lr.right = root
            start = ll
        else:
            start = root
            
        rl, rr = self.demand(root.right)
        if rl is not None:
            root.right = rl
            rl.left = root
            end = rr
        else:
            end = root
            
        return start, end
