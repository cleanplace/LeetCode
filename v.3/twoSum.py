class Solution:
    def twoSum(self, nums, target):
        num_dict = dict()

        for idx, num in enumerate(nums):
            candidate_num = target - num
            if candidate_num in num_dict:
                return [num_dict[candidate_num],idx]
            num_dict[num] = idx
        return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()
    result = s.twoSum(nums,target)

    print(result)