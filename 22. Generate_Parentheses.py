class Solution(object):
	def generateParenthesis(self, n):
		out=[]
		print 'start'
		generater(n,n,"",out)
		return out

def generater(left,right,stri,out):
	if left==0:
		stri+=right*')'
		out.append(stri)
		return
	if left<right:
		generater(left-1,right,stri+'(',out)
		generater(left,right-1,stri+')',out)
	elif left==right:
		generater(left-1,right,stri+'(',out)

s=Solution()
print s.generateParenthesis(3)