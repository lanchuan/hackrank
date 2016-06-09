N=input()
K=input()
x=[]
for i in range(N):
	a=input()
	x.append(a)
x=sorted(x)
res=999999999
for i in range(N-K+1):
	a=x[i+K-1]-x[i]
	if a<res:
		res=a
print(res)