class Solution(object):
	def nextPermutation(self, nums):
		l=len(nums)
		for i in range(l-1,0,-1):
			if nums[i-1]<nums[i]:
				for j in range(l-1,i-1,-1):
					if nums[j]>nums[i-1]:
						swap(nums,i-1,j)
						reverse(nums,i)
						return
		reverse(nums,0)

def swap(lis,a,b):
	temp = lis[a]
	lis[a]=lis[b]
	lis[b]=temp
def reverse(lis,a):
	l=len(lis)
	x=l-a
	for i in range(x/2):
		swap(lis,a+i,l-i-1)

s=Solution()
a=[1,3,2]
b=[3,2,1]
c=[1,1,5]
s.nextPermutation(a)
s.nextPermutation(b)
s.nextPermutation(c)
print a,b,c