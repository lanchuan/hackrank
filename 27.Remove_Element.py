class Solution(object):
	def removeElement(self, nums, val):
		j=0
		for i in nums:
			if i!=val:
				nums[j]=i
				j+=1
		return j

s=Solution()
a=[1]
b=s.removeElement(a,3)
print b,a