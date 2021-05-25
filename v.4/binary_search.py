class Solution(object):
    def search(self, nums, target):

        if (not nums):
            return -1

        pivot_index = self.find_pivot(nums)
        result = self.bin_search(nums, target, 0, pivot_index - 1)

        if (result != -1):
            return result
        else:
            return self.bin_search(nums, target, pivot_index, len(nums) - 1)

    def find_pivot(self, arr):

        element_to_compare = arr[-1]
        low = 0
        high = len(arr) - 1

        while (low <= high):
            mid = (low + high) // 2
            if element_to_compare < arr[mid]:
                low = mid + 1
            elif element_to_compare >= arr[mid]:
                high = mid - 1

        return low

    def bin_search(self, arr, value, low, high):
        while (low <= high):
            mid = int((low + high) / 2)
            if value < arr[mid]:
                high = mid - 1
            elif value > arr[mid]:
                low = mid + 1
            else:
                return mid
        return -1


# 투포인터
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = int((end + start) / 2)
            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end] :
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    s = Solution()
    print(s.search(nums, target))