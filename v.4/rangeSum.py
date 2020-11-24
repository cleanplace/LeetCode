class Solution:
    def rangeSum(self, nums, n, left, right):
        i, j, amount = 0, 0, 0
        total_sum = []

        while i < len(nums):
            if j == len(nums) - 1:
                amount += nums[j]
                total_sum.append(amount)
                i += 1
                j = i
                amount = 0
            else:
                if i == j:
                    amount = nums[j]
                    total_sum.append(amount)
                    j += 1
                else:
                    amount += nums[j]
                    total_sum.append(amount)
                    j += 1

        total_sum.sort()
        return sum(total_sum[left - 1:right]) % (10 ** 9 + 7)

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 5

    s=Solution()
    print(s.rangeSum(nums,n,left,right))

