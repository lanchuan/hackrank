a,b=[int(x) for x in raw_input().split()]
result=0
for i in range(b):
	x,y,z=[int(k) for k in raw_input().split()]
	result+=(y-x+1)*z
print result/a