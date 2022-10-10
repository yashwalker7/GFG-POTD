class Solution:
    def decodedString(self, s):
        # code here
        a=[]
        i=0
        res=''
        while(i<len(s)):
            if (s[i]==']'):
                b =''
                while (a[-1]!= '['):
                    b=a.pop()+b
                a.pop()
                m=''
                while (a and a[-1].isdigit()):
                    m=a.pop()+m
                res=b*int(m)
                a.append(res)
            else:
                a.append(s[i])
            i+=1
        if(res==''):
            return s
        res=''
        for i in range(len(a)):
            res=a[i]+res
        return res
