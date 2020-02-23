class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        Num = [float('inf') for _ in range(amount + 1)]

        Num[0] = 0

        for idx in range(amount + 1):
            for coin in coins:
                if coin <= idx:
                    Num[idx] = min(Num[idx], Num[idx - coin] + 1)

        if Num[amount] == float('inf'):
            return -1
        else:
            return Num[idx]