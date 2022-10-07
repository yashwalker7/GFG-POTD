class Solution:
    def countOfSubstrings(self, S, K):
        # code here 
        c=0
        n=len(S)
        d={}
        i=j=0
        while i<K:
            if S[i] in d:
                d[S[i]]+=1
            else:
                d[S[i]]=1
            i+=1
        while i<n:
            if len(d)==K-1:
                c+=1
            d[S[j]]-=1
            if d[S[j]]==0:
                del d[S[j]]
            if S[i] in d:
                d[S[i]]+=1
            else:
                d[S[i]]=1
            i+=1
            j+=1
        if len(d)==K-1:
            c+=1
        return c
