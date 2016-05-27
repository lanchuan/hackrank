class Solution(object):
	def longestValidParentheses(self, s):

		stack=[]
		for i in range (0, len(s)):
			if not stack: stack.append(i)
			else:
				if s[i] ==")" and s[stack[-1]] == "(":
					stack.pop()
					continue
				stack.append(i)
		end = len(s)
		if not stack: return end
		res = 0
		while stack:
			start = stack.pop()
			res = max(res, end-start-1)
			end = start
		res = max(res, end)
		return res



s=Solution()
a=")("
b="((())()"
c="()"
d="()(()"
e=")()(((())))("
f="(()(((()"
print '___________',s.longestValidParentheses(a),0
print '___________',s.longestValidParentheses(b),6
print '___________',s.longestValidParentheses(c),2
print '___________',s.longestValidParentheses(d),2
print '___________',s.longestValidParentheses(e),10
print '___________',s.longestValidParentheses(f),2