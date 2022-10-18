#User function Template for python3

'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''

class Solution:
    def sortedListToBST(self, head):
        #code here
        def fun(low,high,a):
            if((low+high)%2==0):
                mid=(low+high)//2
                return mid
            else:
                mid=(low+high)//2
                return mid+1
        a=[]
        temp=head
        while(temp):
            a.append(temp.data)
            temp=temp.next
        def make(low,high,a):
            if(low>high):
                return None
            mid=fun(low,high,a)
            root=TNode(a[mid])
            root.left=make(low,mid-1,a)
            root.right=make(mid+1,high,a)
            return root
        return make(0,len(a)-1,a)
