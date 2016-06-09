T=input()

for i in range(T):
	N=input()
	def deal(N):
		K=0
		while N%3!=0:
			N=N-5
			K=K+5
			if N<0:
				return -1
		return '5'*N+'3'*K
	print deal(N)
