# Expand Around Center
class Solution():
    def longestPalindrome(self,s):
        res = ""
        for i in range(len(s)):
            odd = palindromeAt(s, i, i)
            even = palindromeAt(s, i, i + 1)

            res = max(res, odd, even, key=len)
        return res
#
#
# starting at l,r expand outwards to find the biggest palindrome
def palindromeAt(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]


# Manacher's Algorithm
class Solution():
    def longestPalindrome(self, s: str) -> str:
        t = '^#'+'#'.join(s)+'#$'
        n = len(t)
        p = [0]*n
        c = r = cm = rm = 0

        for i in range (1, n-1):
            p[i] = min(r-i, p[2*c-i]) if r > i else 0
            while t[i-p[i]-1] == t[i+p[i]+1]: p[i] += 1
            if p[i]+i > r: c, r = i, p[i]+i
            if p[i] > rm: cm, rm = i, p[i]

        return s[(cm-rm)//2:(cm+rm)//2]


if __name__ == "__main__":
    input1= "babad"
    input2 = "cbbd"

    s = Solution()
    result = s.longestPalindrome(input2)

    print(result)