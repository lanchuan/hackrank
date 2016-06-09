T=input()
for i in range(T):
	res=0
	N,C,M=[int(x) for x in raw_input().split()]
	res+=N/C
	wrap=res
	a=wrap/M
	while a!=0:
		res+=a
		wrap=wrap%M+a
		a=wrap/M
	print res

