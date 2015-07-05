# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in place.
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        marcar = []
        for i in range(len(matrix)) :
            for j in range(len(matrix[i])) :
                if matrix[i][j] == 0 :
                    marcar.append((i,j))
        for t in marcar :
            self.setRowsZeroes(matrix, t[0])
            self.setColsZeroes(matrix, t[1])
    def setRowsZeroes(self, matrix, row):
        for i in range(len(matrix[row])) :
            matrix[row][i] = 0
    def setColsZeroes(self, matrix, col):
        for i in range(len(matrix)) :
            matrix[i][col] = 0

if __name__ == "__main__" :
    m = [
        [1, 2, 3, 1],
        [5, 0, 6, 7],
        [8, 9, 3, 1]
    ]
    s = Solution()
    s.setZeroes(m)
    for i in range(len(m)) :
        for j in range(len(m[i])) :
            print (m[i][j], end=" ")
        print ()
