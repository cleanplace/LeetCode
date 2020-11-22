def sub_array(nums, i, total, S):
    if i == len(nums):
        if total == S:
            return 1
        return 0

    a = sub_array(nums, i + 1, total + nums[i], S)
    b = sub_array(nums, i + 1, total - nums[i], S)

    return a + b


class Solution:

    def findTargetSumWays(self, nums, S) :
        answer = sub_array(nums, 0, 0, S)
        return answer

if __name__ == "__main__":

    input = [1, 1, 1, 1, 1]
    s = Solution()
    print(s.findTargetSumWays(input,3))
