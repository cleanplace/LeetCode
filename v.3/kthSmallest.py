"""
378. Kth Smallest Element in a Sorted Matrix
"""

### Min-Heap approach
# O(Klog(N))/O(N)
# X=min(K,N); X+Klog(X)/O(X)

import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        N = len(matrix)

        element = 0
        minHeap = []

        for r in range(min(k, N)):
            minHeap.append((matrix[r][0], r, 0))

        heapq.heapify(minHeap)

        while k:
            element, r, c = heapq.heappop(minHeap)

            if c < N - 1:
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))

            k -= 1

        return element

if __name__ == "__main__":
    a = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    s = Solution()
    result = s.kthSmallest(a,8)

    print(result)