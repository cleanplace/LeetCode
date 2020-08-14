"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

* Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

* Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""

class Solution:
    def merge(self, intervals) :

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:

            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    s= Solution()
    result = s.merge(intervals)
    print(result)