# HashMap
# O(N)/O(N)
# import collections
#
# class Solution:
#     def majorityElement(self, nums):
#         counts = collections.Counter(nums)
#         return max(counts.keys(), key=counts.get)

# Sorting
# O(NlogN)/O(1)
# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums)//2]

# Divide and Conquer
#O(NlogN)/O(logN)
class Solution:
    def majorityElement(self, nums):
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        a = self.majorityElement_(nums[:len(nums) // 2])
        b = self.majorityElement_(nums[len(nums) // 2:])

        if a == b:
            return a
        return [b, a][nums.count(a) > len(nums) // 2]

    # the idea here is if a pair of elements from the
    # list is not the same, then delete both, the last
    # remaining element is the majority number
    def majorityElement_(self, nums):
        count, cand = 0, 0
        for num in nums:
            if num == cand:
                count += 1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        return cand


if __name__ == "__main__":
    #nums = [3, 2, 3]
    nums = [2, 2, 1, 1, 1, 2, 2]
    s = Solution()
    print(s.majorityElement(nums))
