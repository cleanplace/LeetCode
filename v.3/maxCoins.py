# Top-down
class Solution:
    def maxCoins(self, nums):

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1:
                return dp[i][j]
            coins = 0
            for k in range(i+1, j):
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)


# Bottom-up
class Solution(object):
    def maxCoins(self, nums):

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n - 1]

if __name__ == "__main__":
    input = [3, 1, 5, 8]
    s = Solution()
    print(s.maxCoins(input))
