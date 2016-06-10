T=input()
for i in range(T):
	year=input()
	l=1
	for j in range(year):
		if j%2==0:
			l=l*2
		else:
			l=l+1
	print l