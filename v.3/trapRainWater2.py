"""
407. Trapping Rain Water II

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.

** Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

"""
import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1: #테두리면은...
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1

        result = 0
        while heap: #힙의 원소가 없을때까지 반복
            height, i, j = heapq.heappop(heap)  #테두리 값부터 작은것부터 빠진다.
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]: #메트릭스 안에 있으면서 방문 안한 것을 탐색
                    result += max(0, height - heightMap[x][y]) #양각인지 음각인지 구별
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y)) #탐색할 대상에 새롭게 추가 , #수면을 찾기 위해 max값을 업데이트해가며...
                    visited[x][y] = 1
        return result

if __name__ == "__main__":
    trap =[[1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]]

    s=Solution()
    result=s.trapRainWater(trap)

    print(result)