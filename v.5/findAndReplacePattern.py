class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            P = {}
            return [P.setdefault(c, len(P)) for c in word]
        return [w for w in words if match(w) == match(pattern)]

if __name__ == "__main__":

    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"

    s = Solution()
    print(s.findAndReplacePattern(words, pattern))