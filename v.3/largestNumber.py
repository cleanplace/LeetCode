"""
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

* Example 1:
Input: [10,2]
Output: "210"

* Example 2:
Input: [3,30,34,5,9]
Output: "9534330"

"""

class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

if __name__ == "__main__":
    input=[3, 30, 34, 5, 9]

    s = Solution()
    result = s.largestNumber(input)

    print(result)