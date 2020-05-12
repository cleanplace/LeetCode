"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1] * m for i in range(n)]

        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]

