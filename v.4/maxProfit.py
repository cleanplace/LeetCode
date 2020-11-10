class Solution:
    def maxProfit(self, prices):

        if len(prices) <= 1:
            return 0

        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
                #esult.append(profit)

        return profit


if __name__ == "__main__":
    input = [7,1,5,3,6,4]

    s = Solution()
    print(s.maxProfit(input))


