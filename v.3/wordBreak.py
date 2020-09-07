class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i] and s[i: j + 1] in wordDict:
                    dp[j + 1] = True

        return dp[-1]

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]

    # s = "applepenapple"
    # wordDict = ["apple", "pen"]

    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]

    a = Solution()
    print(a.wordBreak(s,wordDict))
