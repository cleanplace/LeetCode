"""
376. Wiggle Subsequence

A sequence of numbers is called a wiggle sequence if the differences
between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative.
A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative.
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences,
the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence.
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence,
leaving the remaining elements in their original order.

"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        seq = len(nums)
        postv = False
        negatv = False

        result = 1

        if seq == 0:
            return 0

        for i in range(1, seq):
            if nums[i - 1] < nums[i]:
                postv = True

                if negatv:
                    result += 1
                    negatv = False

            if nums[i - 1] > nums[i]:
                negatv = True

                if postv:
                    result += 1
                    postv = False

        if postv or negatv:
            result += 1

        return result