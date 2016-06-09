T=input()
for i in range(T):
	N=input()
	price=[int(x) for x in raw_input().split()]
	start=0
	pro=0

	def findmax(index):
		max=0
		res=index
		for i in range(index,len(price)):
			if price[i]>max:
				max=price[i]
				res=i
		return res

	while start<len(price):
		big=findmax(start)
		if big!=start:
			pro+=(big-start)*price[big]-sum(price[start:big])
			start=big+1
		else:
			start+=1
	print pro 


