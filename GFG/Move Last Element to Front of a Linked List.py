from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""

class Solution:
    def moveToFront(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        if not head.next:
            return head
        curr = head
        while curr and curr.next and curr.next.next:
            curr = curr.next
        last = curr.next
        curr.next = None
        last.next = head
        return last
