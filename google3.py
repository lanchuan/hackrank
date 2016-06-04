def solution(S):
	stack=[0]
	result=0
	S=S.split("\n")

	def count(line):
		res=0
		for i in line:
			 if i==' ':
			 	res+=1
			 else:
			 	break
		return res
	
	for line in S:
		folder=count(line)
		l=len(line)
		while  folder<len(stack)-1:
			stack.pop()
		stack.append(stack[-1]+len(line)+1-folder)
		
		if (l>5 and line[-5:]=='.jpeg') or (l>4 and line[-4:]=='.gif') or (l>4 and line[-4:]=='.png'):
			result += stack.pop()

	return result
	
print solution('dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif' )