from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        for v in Counter(s).values():
            answer += v // 2 * 2
            if answer % 2 == 0 and v % 2 == 1:
                answer += 1

        return answer



if __name__ == "__main__":
    input = "abccccdd"

    s = Solution()
    print(s.longestPalindrome(input))