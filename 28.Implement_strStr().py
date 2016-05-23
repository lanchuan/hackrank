class Solution(object):
	def strStr(self, haystack, needle):
		if len(haystack)<len(needle):
			return -1
		if needle=="":
			return 0
		for i in range(len(haystack)-len(needle)+1):
			if haystack[i]==needle[0]:
				if compare(haystack[i:],needle):
					return i
		return -1
		
def compare(a,b):
	for i in range(len(b)):
		if a[i]!=b[i]:
			return False
	return True


s=Solution()
a="halloue"
b="ll"
print s.strStr(a,b)
#print compare(a,b)