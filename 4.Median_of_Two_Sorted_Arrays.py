class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        total=m+n
        if total%2==1:
            return findkth(nums1,m,nums2,n,total/2+1)
        else:
            return (float(findkth(nums1,m,nums2,n,total/2+1))+float(findkth(nums1,m,nums2,n,total/2)))/2
        
            
def findkth(a,m,b,n,k):
    if m>n:
        return findkth(b,n,a,m,k)
    if m==0:
        return b[k-1]
    if k==1:
        return min(a[0],b[0])
    pa=min((k/2) ,m)
    pb=k-pa
    if a[pa-1]<b[pb-1]:
        return findkth(a[pa:],m-pa,b,n,k-pa)
    elif a[pa-1]>b[pb-1]:
        return findkth(a,m,b[pb:],n-pb,k-pb)
    else:
        return a[pa-1]