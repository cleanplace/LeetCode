# 53. Maximum Subarray : 최대 부분합 구하기

# 1. Brute Force
import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)

        return max_subarray




# 2. Dynamic Programming, Kadane's Algorithm
# Time complexity: O(N)/O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 배열의 첫번째 요소로 초기화 할 것
        current_subarray = max_subarray = nums[0]

        # 첫번째 요소로 초기화했으니, 숫자 검사는 배열의 두번째부터 진행
        for num in nums[1:]:
            # current_subarray가 음수라면 버리고, 배열의 값을 계속 더해 최대 부분합을 찾아간다.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray


# 3. Divide and Conquer
# Time complexity: O(N⋅logN) / Space complexity: O(logN)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # 초기값으로 무한대 값으로 세팅
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # 중간값에서 0인덱스 순서로 역순으로 for문 돌리기
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # 중간값에서 가장 마지막 인덱스까지 for문 돌리기
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # 왼쪽파트, 오른쪽 파트 그리고 절반 인덱스를 더해서, 최대합을 만듦
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # 오른쪽 절반, 왼쪽 절반을 부분 집합으로 쪼개 최대 부분합을 구함
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # 각 결과의 max값을 리턴
            return max(best_combined_sum, left_half, right_half)

        # 리스트의 전체 입력값으로도 계산
        return findBestSubarray(nums, 0, len(nums) - 1)