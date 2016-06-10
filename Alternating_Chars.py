T=input()
for i in range(T):
	s=raw_input()
	count=0
	for j in range(1,len(s)):
		if s[j]==s[j-1]:
			count +=1
	print count
