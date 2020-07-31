"""
200. Number of Islands

"""


class Solution(object):
    def numIslands(self, grid):

        num_row = len(grid)
        num_col = len(grid[0])

        num_islands = 0

        if len(grid) < 0:
            return 0

        for row in range(num_row):
            for col in range(num_col):
                if grid[row][col] == '1':
                    num_islands += 1
                    self.check_island(row, col, grid)

        return num_islands

    def check_island(self, row, col, grid):

        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == '0':
            # 함수 종료
            return
        else:
            grid[row][col] = '0'

        self.check_island(row, col + 1, grid)
        self.check_island(row, col - 1, grid)
        self.check_island(row + 1, col, grid)
        self.check_island(row - 1, col, grid)

if __name__ == "__main__":
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    s = Solution()
    result = s.numIslands(grid)

    print(result)