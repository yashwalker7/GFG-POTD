    def minChar(self,str):
        n=len(str)
        i=0
        j=n-1
        var=n-1
        while(i<j):
            if str[i]==str[j]:
                i=i+1
                j=j-1
            else:
                i=0
                var=var-1
                j=var
        return n-var-1
        #Write your code here
