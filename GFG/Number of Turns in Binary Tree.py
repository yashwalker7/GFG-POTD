class Solution:
    def NumberOFTurns(self, root, first, second):
        #return the number of turns required to go from first node to second node
        res = ''
        def lca(a,b,c):
            if not a:
                return
            if a.data==c or a.data==b:
                return a
            left = lca(a.left,b,c)
            right  = lca(a.right,b,c)
            if left is None:
                return right
            if right is None:
                return left
            return a
        x = lca(root,first,second)
        
        def height(a,t,s):
            nonlocal res
            if not a:
                return False
           
            if a.data==t:
                res = s
                return res
            if a.left:
                height(a.left,t,s+'L')
            if a.right:
                height(a.right,t,s+'R')
        
        r = height(x,first,'')
        r = res
        res = ''
        height(x,second,'')
        p = res
        r1,p1 = 0,0
        for i in range(1,len(r)):
            if r[i]!=r[i-1]:
                r1+=1
        for i in range(1,len(p)):
            if p[i]!=p[i-1]:
                p1+=1
        
        if x.data==first:
            return p1
        elif x.data==second:
            return r1
        return r1+p1+1
