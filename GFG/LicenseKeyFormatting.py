
class Solution:
    def ReFormatString(self,S, K):
        #code here
        a,j=0,0
        c=[]
        d=''
        for i in range(len(S)-1,-1,-1):
            if S[i]!='-':
                d+=S[i].upper()
                a+=1
            if(a==K):
                c.append(d[::-1])
                a=0
                d=''
        if(a<K and a!=0):
            c.append(d[::-1])
        c=c[::-1]
        return '-'.join(c)