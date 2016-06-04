class Solution(object):
	def solveSudoku(self, board):
		d={}

		def check():
			for i in range(9):
				l=[]
				for j in range(9):
					if board[i][j]=='.':
						d[(i,j)]=[1,2,3,4,5,6,7,8,9]
						l.append(0)
					else:
						l.append(int(board[i][j]))
				board[i]=l
			print board
			print d

		def checkrow():
			for i in range(9):
				l=[]
				for j in range(9):
					if board[i][j]!=0:
						l.append(board[i][j])
				print l
				for k in range(9):
					if board[i][k]==0:
						for x in l:
							if x in d[(i,k)]:
								d[(i,k)].remove(x)
						if len(d[(i,k)])==1:
							board[i][k]=d[(i,k)][0]
							d.pop((i,k),None)
			print d
		def checkcolum():
			for j in range(9):
				l=[]
				for i in range(9):
					if board[i][j]!=0:
						l.append(board[i][j])
				for k in range(9):
					if board[k][j]==0:
						for x in l:
							if x in d[(k,j)]:
								d[(k,j)].remove(x)
						if len(d[(k,j)])==1:
							board[k][j]=d[(k,j)][0]
							d.pop((k,j),None)
		def checkblock():
			for i in range(3):
				for j in range(3):
					l=[]
					for k in range(3):
						for m in range(3):
							if board[i*3+k][j*3+m]!=0:
								l.append(board[i*3+k][j*3+m])
					for n in range(3):
						for o in range(3):
							if board[i*3+n][j*3+o]==0:
								for x in l:
									if x in d[(i*3+n,j*3+o)]:
										 d[(i*3+n,j*3+o)].remove(x)
								if len( d[(i*3+n,j*3+o)])==1:
									board[i*3+n][j*3+o]=d[(i*3+n,j*3+o)][0]
									d.pop((i*3+n,j*3+o),None)
		check()
		while d:
			si=len(d)
			checkrow()
			checkcolum()
			checkblock()
			if len(d)==si:
				print board
				break

s=Solution()
a=["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
s.solveSudoku(a)
print a

