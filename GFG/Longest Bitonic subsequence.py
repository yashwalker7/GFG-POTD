class Solution:
	def LongestBitonicSequence(self, nums):
		# Code here
		list1=[1]*len(nums)
		for i in range(len(nums)):
		    for j in range(0,i):
		        if nums[i]>nums[j]:
		            list1[i]=max(list1[i],list1[j]+1)
		list2=[1]*len(nums)
		for l in range(len(nums)-1,-1,-1):
		    for m in range(l+1,len(nums)):
		        if nums[l]>nums[m]:
		            list2[l]=max(list2[l],list2[m]+1)
		            
		final=[]
		for k in range(len(list1)):
		    temp=(list1[k]+list2[k])-1
		    final.append(temp)
		return max(final)
