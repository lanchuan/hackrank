T=input()
res=list('abcdefghijklmnopqrstuvwxyz')
# res
for i in range(T):
	x=raw_input()
	res=[j for j in res if j in x ]
print res,len(res)