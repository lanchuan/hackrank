class Solution(object):
	def rotate(self, nums, k):
		l=len(nums)
		k=k%l
		
		def swap(i,j):
			while i<j:
				nums[i],nums[j]=nums[j],nums[i]
				i+=1
				j-=1

		swap(0,l-k-1)
		swap(l-k,l-1)
		swap(0,l-1)

s=Solution()
a=[1,2,3]
k=1
s.rotate(a,k)
print a