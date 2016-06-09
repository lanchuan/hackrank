T=input()
for i in range(T):
	target=raw_input()
	res=0
	a=[int(x) for x in target]
	for j in a:
		target=int(target)
		if j!=0 and target%j==0:
			res+=1
	print res