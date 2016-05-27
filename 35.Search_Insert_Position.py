class Solution(object):
	def searchInsert(self, nums, target):
		start=0
		end=len(nums)-1
		res=0
		while start+1<end:
			mid=(start+end)/2
			if nums[mid]==target:
				return mid
				break
			elif nums[mid]<target:
				start=mid
			elif nums[mid]>target:
				end=mid
		if nums[start]==target:
			return start
		elif nums[end]==target:
			return end
		if nums[end]<target:
			return end+1
		elif nums[start]>target:
			return start
		else:return start+1


s=Solution()
a=[1,3,5,6]
print s.searchInsert(a,5),'2'
print s.searchInsert(a,2),'1'
print s.searchInsert(a,7),'4'
print s.searchInsert(a,0),'0'