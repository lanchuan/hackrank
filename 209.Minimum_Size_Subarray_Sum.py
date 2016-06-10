class Solution(object):
	def minSubArrayLen(self, s, nums):
		start=end=0
		l=len(nums)
		if l==0:
			return 0
		su=nums[0]
		res=999999
		temp=1
		while start<l:
			print start,end,su
			if su<s:
				if end<l-1:
					end+=1
					su+=nums[end]
					temp+=1
				else:
					break
			else:
				if temp<res:
					res=temp			
				su-=nums[start]
				start+=1
				temp-=1
		if res<999999:
			return res
		else:
			return 0

s=Solution()
a=4
b=[1,4,4]
print s.minSubArrayLen(a,b)