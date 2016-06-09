N=input()
A=[int(x) for x in raw_input().split()]
B=[]
for i in A:
	if i in B:
		B.remove(i)
	else:
		B.append(i)
for j in B:
	print j 