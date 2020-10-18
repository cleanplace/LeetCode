class Solution:
    def productExceptSelf(self, nums):

        p = 1
        length_nums = len(nums)
        output = []

        for i in range(0, length_nums):
            output.append(p)
            p = p * nums[i]

        p = 1
        for i in range(length_nums - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

if __name__ == "__main__":

    nums=[1,2,3,4]
    a = Solution()
    print(a.productExceptSelf(nums))
