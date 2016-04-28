a=input()
flag=False
maxstick=0
sumstick=0
num=0
l=[]
for i in range(a):
	stick=[int(i) for i in raw_input().strip().split()]
	if stick[0]==1:
		sumstick+=stick[1]
		num+=1
		l.append(stick[1])
	else:
		sumstick-=stick[1]
		num-=1
		l.remove(stick[1])
	if num<3:
		flag=False
	elif sum(l)-max(l)>max(l):
			flag=True
	else:
		flag=False
	print flag