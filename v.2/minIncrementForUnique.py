"""
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.


Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


Note:

0 <= A.length <= 40000
0 <= A[i] < 40000

"""


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:

        n = len(A)

        if n < 2:
            return 0

        ans = 0
        dup = []

        count = collections.Counter(A)

        i = min(count)
        end = max(count)

        while dup or i <= end:

            if count[i] >= 2:
                dup.extend([i] * (count[i] - 1))
            elif dup and count[i] == 0:
                ans += i - dup.pop()

            i += 1

        return ans