"""
# DFS recursively
class Solution(object):
    def subsets(self, nums):
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, path, result):
        result.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], path + [nums[i]], result)
"""
# Bit Manipulation
class Solution(object):
    def subsets(self, nums):
        result = []
        nums.sort()
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            result.append(tmp)
        return result


if __name__ == "__main__":

    nums = [1, 2, 3]
    s = Solution()
    print(s.subsets(nums))