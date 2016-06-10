class Solution(object):
	def rotate(self, matrix):
		l=len(matrix)
		for i in range(l-1):
			for j in range(i,l-1-i):
				matrix[j][l-1-i],matrix[l-1-i][l-1-j],matrix[l-1-j][i],matrix[i][j]=matrix[i][j],matrix[j][l-1-i],matrix[l-1-i][l-1-j],matrix[l-1-j][i]