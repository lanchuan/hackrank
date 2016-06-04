N=int(input())
fibo=[1,1]
for i in range(N):
	a=int(input())
	while fibo[-1]<a:
		fibo.append(fibo[-1]+fibo[-2])
	if a in fibo:
		print "IsFibo"
	else:
		print "IsNotFibo"