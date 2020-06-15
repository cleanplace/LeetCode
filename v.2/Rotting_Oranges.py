"""
994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead

*Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

*Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten = []
        # 썩은 오랜지 위치값 구하기
        rows, columns = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        # 썩은 오랜지 위치 값을 기본으로하여, 상할 가능성이 있는 이웃 오랜지값 구하기
        def add_neighbors(rotten):
            neighbors = []
            for i, j in rotten:
                if i > 0 and grid[i - 1][j] == 1:
                    neighbors.append((i - 1, j))
                    grid[i - 1][j] = 2
                if j > 0 and grid[i][j - 1] == 1:
                    neighbors.append((i, j - 1))
                    grid[i][j - 1] = 2
                if i < rows - 1 and grid[i + 1][j] == 1:
                    neighbors.append((i + 1, j))
                    grid[i + 1][j] = 2
                if j < columns - 1 and grid[i][j + 1] == 1:
                    neighbors.append((i, j + 1))
                    grid[i][j + 1] = 2
            return neighbors

        # 상해 가는 시간 구하기
        minutes = 0
        while (1):
            rotten = add_neighbors(rotten)
            if len(rotten) == 0:
                break
            minutes += 1

        # 전체 행,렬을 돌면서 혹시라도 싱싱한 오랜지가 있는지 검사
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    return -1

        return minutes
