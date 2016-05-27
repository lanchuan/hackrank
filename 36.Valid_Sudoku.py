class Solution(object):
	def isValidSudoku(self, board):

		for i in board:
			s=[]
			for j in i:
				if j!='.':
					if j not in s and j !='.':
						s.append(j)
					else: return False
		for j in range(9):
			s=[]
			for i in range(9):
				if board[i][j]!='.':
					if board[i][j] not in s:
						s.append(board[i][j])
					else:return False
		for i in range(3):
			for j in range(3):
				s=[]
				for k in range(3):
					for h in range(3):
						if board[3*i+k][3*j+h]!='.':
							if board[3*i+k][3*j+h] not in s:
								s.append(board[3*i+k][3*j+h] ) 
							else:return False
		return True

s=Solution()
a=[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print s.isValidSudoku(a)