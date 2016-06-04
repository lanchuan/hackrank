def solution(X):
	a=str(X)
	print a
	for i in range(len(a)-1):
		if a[i+1]<a[i]:
			if i==len(a)-2:
				a=a[:-1]
				return int(a)
			a=a[:i+1]+a[i+2:]
			return int(a)
		
print solution(23361)