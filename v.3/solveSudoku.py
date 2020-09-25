class Solution:
    def solveSudoku(self, board):
        self.board = board
        self.val = self.PossibleVals()
        self.Solver()

    def PossibleVals(self): # 답이 가능한 후보군을 리턴
        a = "123456789"
        d, val = {}, {}
        for i in range(9):
            for j in range(9):
                ele = self.board[i][j]
                if ele != ".":
                    d[("r", i)] = d.get(("r", i), []) + [ele]
                    d[("c", j)] = d.get(("c", j), []) + [ele]
                    d[(i // 3, j // 3)] = d.get((i // 3, j // 3), []) + [ele]
                else:
                    val[(i, j)] = []
        for (i, j) in val.keys():
            inval = d.get(("r", i), []) + d.get(("c", j), []) + d.get((i / 3, j / 3), [])
            val[(i, j)] = [n for n in a if n not in inval]
        return val

    def Solver(self):
        if len(self.val) == 0:
            return True
        key = min(self.val.keys(), key=lambda x: len(self.val[x]))# 가능한 답들이 담겨있는 리스트에서 길이가 가장 최소인 리스트 먼저 계산(답 후보군이 될 것들이 적은거)
        nums = self.val[key]
        for n in nums:
            update = {key: self.val[key]}
            if self.ValidOne(n, key, update):  # 가능한 답 한개를 선택
                if self.Solver():  # keep solving
                    return True
            self.undo(key, update)  # 가능하지 않은 답이면 한 단계 돌아감
        return False

    def ValidOne(self, n, kee, update):
        self.board[kee[0]][kee[1]] = n
        del self.val[kee]
        i, j = kee
        for ind in self.val.keys():
            if n in self.val[ind]:
                if ind[0] == i or ind[1] == j or (ind[0] / 3, ind[1] / 3) == (i / 3, j / 3):
                    update[ind] = n
                    self.val[ind].remove(n)
                    if len(self.val[ind]) == 0:
                        return False
        return True

    def undo(self, kee, update):
        self.board[kee[0]][kee[1]] = "."
        for k in update:
            if k not in self.val:
                self.val[k] = update[k]
            else:
                self.val[k].append(update[k])
        return None

if __name__ == "__main__":

    bord= [["5", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    s = Solution()
    s.solveSudoku(bord)

    print(s.solveSudoku(bord))