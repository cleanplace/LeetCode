class Solution:
    def sub_array(nums, i, total, S):
        if i == len(nums):
            if total == 0:
                return 1
            return 0

        a = sub_array(nums, i + 1, total + nums[i], S)
        b = sub_array(nums, i + 1, total - nums[i], S)

        return a + b

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        answer = sub_array(nums, 0, 0, S)
        return answer