class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        i = 0
        for j in range(len(s)):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            if maxCost < 0:
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        return (len(s)-1) - i + 1

if __name__ == "__main__":
    #s = "abcd"
    #t = "bcdf"
    s = "abcd"
    t = "cdef"
    maxCost = 3

    a = Solution()
    result =a.equalSubstring(s,t,maxCost)

    print(result)