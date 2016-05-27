class Solution(object):
    def searchRange(self, nums, target):
    	if not nums:return [-1,-1]
    	start=0
    	end=len(nums)-1
    	res1=-1
    	res2=-1
    	while start+1<end:
    		mid=(start+end)/2
    		if nums[mid]==target:
    			if nums[mid-1]<target:
    				res1=mid
    				break
    			else:
    				end=mid
    		elif nums[mid]>target:
    			end=mid
    		else:
    			start=mid
    	if res1==-1:
    		if nums[start]==target:
    			res1=start
    		elif nums[end]==target:
    			res1=end
    	start=0
    	end=len(nums)-1
    	while start+1<end:
    		mid=(start+end)/2
    		if nums[mid]==target:
    			if nums[mid+1]>target:
    				res2=mid
    				break
    			else:
    				start=mid
    		elif nums[mid]>target:
    			end=mid
    		else:
    			start=mid
    	if res2==-1:
    		if nums[end]==target:
    			res2=end
    		elif nums[start]==target:
    			res2=start
    	return [res1,res2]

s=Solution()
a=[5, 7, 7, 8, 8, 10]
b=[1,2,2]
c=[3,3,3]
print s.searchRange(a,8)
print s.searchRange(b,2)
print s.searchRange(c,3)