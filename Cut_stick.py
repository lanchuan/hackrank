N=input()
A=[int(x) for x in raw_input().split()]
A=sorted(A)
index=1
print len(A)
while index<len(A):
	if A[index-1]== A[index]:
		index+=1
	else:
		print len(A)-index
		index+=1
