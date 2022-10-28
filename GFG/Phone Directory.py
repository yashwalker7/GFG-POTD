
class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        contact=list(set(contact))
        a=""
        output=[]
        for i in range(len(s)):
            a+=s[i]
            temp=[]
            l=len(a)
            for j in contact:
                   if j[:l]==a:
                       temp.append(j)
            if bool(temp)==False:
                 output.append([0])
            else:
                temp.sort()
                output.append(temp)
        return output
