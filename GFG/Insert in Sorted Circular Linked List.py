class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def sortedInsert(self, h, data):
        nn = Node(data)
        if not h:
            nn.next = nn
            return nn
            
        c = h
        while True:
            if c.data <= data <= c.next.data:
                break
            elif c.next == h:
                break
            c = c.next
            
        nn.next = c.next
        c.next = nn
        
        if nn.data < h.data:
            h = nn
        return h
