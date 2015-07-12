class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        for i in range(9) :
            valores = []
            for j in range (9) :
                if board[i][j] != "." :
                    if board[i][j] in valores :
                        return False
                    valores.append(board[i][j])
        for j in range(9) :
            valores = []
            for i in range (9) :
                if board[i][j] != "." :
                    if board[i][j] in valores :
                        return False
                    valores.append(board[i][j])
        for p1 in range (3) :
            for p2 in range (3) :
                valores = []
                for i in range (p1*3, (p1+1)*3) :
                    for j in range (p2*3, (p2+1)*3) :
                        if board[i][j] != "." :
                            if board[i][j] in valores :
                                return False
                            valores.append(board[i][j])
        return True

if __name__ == "__main__" :
    s = Solution()
    sudokus = [
        [
            "....5..1.",
            ".4.3.....",
            ".....3..1",
            "8......2.",
            "..2.7....",
            ".15......",
            ".....2...",
            ".2.9.....",
            "..4......"
        ]
    ]
    for sudoku in sudokus :
        print(s.isValidSudoku(sudoku))
