#User function Template for python3


#Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):
    # Code here
    if root is None:
        return []
    res = []
    s1 = [root]
    s2 = []
    while s1 or s2:
        while s1:
            node = s1.pop()
            res.append(node.data)
            if node.right:
                s2.append(node.right)
            if node.left:
                s2.append(node.left)
        while s2:
            node = s2.pop()
            res.append(node.data)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
    return res



