"""
Given a m * n matrix mat of integers,
sort it diagonally in ascending order
from the top-left to the bottom-right
then return the sorted array.

"""
import collections

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        n, m = len(mat), len(mat[0])

        d = collections.defaultdict(list)

        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])

        for k in d:
            d[k].sort(reverse=1)

        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i - j].pop()

        return mat