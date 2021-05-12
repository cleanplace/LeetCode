"""
560. Subarray Sum Equals K
"""

class Solution(object):
    def subarraySum(self, nums, k):

        tmp_dict = {0: 1}
        sum = 0
        ans = 0

        for i, n in enumerate(nums):
            sum += nums[i]
            if sum - k in tmp_dict:
                ans += tmp_dict[sum - k]
            if sum in tmp_dict:
                tmp_dict[sum] += 1
            else:
                tmp_dict[sum] = 1

        return ans


if __name__ == "__main__":

    # nums = [1, 1, 1]
    # k = 2

    # nums = [1, 2, 3]
    nums = [1,2,1,3]
    k = 3

    s = Solution()
    print(s.subarraySum(nums,k))

    # Time complexity : O(n)
    # Space complexity : O(n)

