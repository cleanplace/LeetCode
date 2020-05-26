"""
Given a circular array (the next element of the last element is the first element of the array),
print the Next Greater Number for every element.
The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]

Explanation:
The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.

"""

import copy

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        res = copy.copy(nums)

        for i in range(0, len(nums)):
            res[i] = -1
            for j in range(1, len(nums)):
                if nums[(i + j) % len(nums)] > nums[i]:
                    res[i] = nums[(i + j) % len(nums)]
                    break

        return res