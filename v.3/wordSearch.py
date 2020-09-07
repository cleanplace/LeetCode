class Solution:
    def exist(self, board, word):
        r = len(board)
        c = len(board[0])

        def isValid(i, j, idx, visited):
            if (i, j) in visited:
                return False

            if idx == len(word):
                return True
            elif i < 0 or i >= r or j < 0 or j >= c:
                return False
            elif board[i][j] == word[idx]:
                return isValid(i + 1, j, idx + 1, visited + [(i, j)]) or \
                       isValid(i - 1, j, idx + 1,visited + [(i, j)]) or \
                       isValid(i,j + 1,idx + 1,visited + [(i,j)]) or \
                       isValid(i, j - 1, idx + 1, visited + [(i, j)])
            else:
                return False

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if isValid(i, j, 0, []): return True
        return False

if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    s = Solution()
    print(s.exist(board,word))