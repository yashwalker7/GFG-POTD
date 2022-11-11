#User function Template for python3

class Solution:
	def characterReplacement(self, s, k):
		# Code here
		a=b=maxlen=ans=0
		Map={}
		while b<len(s):
		    if s[b] in Map:
		        Map[s[b]]+=1
		    else:
		        Map[s[b]]=1
		    maxlen=max(maxlen, Map[s[b]])
		    if ((b-a+1)-maxlen>k):
		        Map[s[a]]-=1
		        a+=1
		    ans=max(ans,b-a+1)
		    b+=1
		return ans
		    
