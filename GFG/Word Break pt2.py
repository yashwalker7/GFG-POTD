class Solution:
    def wordBreak(self, n, dic, s):
        ans=[]
        dic=set(dic)
        def helper(i,path,word):
            if i==len(s):
                if word in dic:
                    ans.append(path)
                    return
                else:
                    return
            if word in dic:
                helper(i+1,path+" "+s[i],s[i])
                helper(i+1,path+s[i],word+s[i])
            else:
                helper(i+1,path+s[i],word+s[i])
        helper(0,"","")
        return ans
