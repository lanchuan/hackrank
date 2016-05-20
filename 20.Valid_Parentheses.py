class Solution(object):
	def isValid(self, s):
		a=[]
		d={'(':')','[':']','{':'}'}
		for i in s:
			if i=='(' or i=='[' or i=='{':
				a.append(i)
			elif a!=[] and d[a[-1]]==i:
				a.pop()
			else:
				return False
		if a==[]:
			return True
		else:
			return False

s=Solution()
print s.isValid("([{}])")