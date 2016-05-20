class Solution(object):
	def fourSum(self, nums, target):
		"""
		type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		        """
		x=len(nums)
		nums=sorted(nums)
		print nums
		result=[]
		k=0
		m=0
		for i in range(0,x-3):
			if 4*nums[i]>target:
				break
			for j in range(x-1,i+2,-1):
				if 4*nums[j]<target:
					break
				k=i+1
				m=j-1
				while(k<m):
					if nums[i]+nums[j]+nums[k]+nums[m]<target:
						k+=1
					elif nums[i]+nums[j]+nums[k]+nums[m]>target:
						m-=1
					else:
						a=[nums[i],nums[k],nums[m],nums[j]]
						if a not in result:
							result.append(a)
						k+=1
						m-=1
		return result

s=Solution()
a=[1,0,-1,0,-2,2]
b=[0,0,0,0]
#print s.fourSum(a,0)
print s.fourSum(b,0)