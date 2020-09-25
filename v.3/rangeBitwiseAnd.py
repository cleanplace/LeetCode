#O(1)/O(1)
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i

if __name__ == "__main__":
    s = Solution()
    print(s.rangeBitwiseAnd(5,7))