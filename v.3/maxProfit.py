class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = 999999
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice

        return maxprofit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(prices))