class Solution:
    def flatten(self, root):
        #code here
        head=root
        while(root):
            d=root
            temp=root.right
            root.right=root.left
            root.left=None
            while(root.right):
                root=root.right
            root.right=temp
            root=d.right
        return head
