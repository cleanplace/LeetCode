"""
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

* Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""

#sorting
#O(NlogN)/O(N)

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort() # python sort 시간복잡도 : O(NlogN)

        longest_sequence = 1
        current_sequence = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_sequence += 1
                else:
                    longest_sequence = max(longest_sequence, current_sequence)
                    current_sequence = 1

        return max(longest_sequence, current_sequence)


if __name__ == "__main__":

    num_list = [100, 4, 200, 1, 3, 2]
    s = Solution()
    result = s.longestConsecutive(num_list)

    print(result)