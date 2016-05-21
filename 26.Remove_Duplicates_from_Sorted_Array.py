class Solution(object):
	def removeDuplicates(self, nums):
		if nums==[]:
			return 0
		j=1
		for i in range(1,len(nums)):
			if nums[i]!=nums[i-1]:
				nums[j]=nums[i]
				j+=1
		return j
a=[1,2,3,3,4,5]
s=Solution()
print s.removeDuplicates(a)