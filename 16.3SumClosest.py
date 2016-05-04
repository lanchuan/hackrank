class Solution(object):
    def threeSumClosest(self, nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=2:
        	return 0
        result=9999
        nums.sort()
        i=0
       	while i< len(nums)-2:
        	j=i+1
        	k=len(nums)-1
        	while j<k:
        		if abs(target-nums[i]-nums[j]-nums[k])<abs(result-target):
        				result=nums[i]+nums[j]+nums[k]
        		if nums[i]+nums[j]+nums[k]<target:
        			j+=1
        		elif nums[i]+nums[j]+nums[k]>target:
        			k-=1
        		else:
        			return target
        			j+=1
        			k-=1
        			while j<k and nums[j]==nums[j-1]:
        				j+=1
        			while j<k and nums[k]==nums[k+1]:
        				k-=1
        	while i <len(nums)-2 and nums[i]==nums[i+1]:
        		i+=1
        	i+=1
        return result
s=Solution()
x=[1,1,1,0]
print s.threeSumClosest(x,-100)
