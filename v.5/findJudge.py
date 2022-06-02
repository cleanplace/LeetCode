class Solution:
    def findJudge(self, N, trust):

        Trusted = [0] * (N + 1)

        for (a, b) in trust:
            Trusted[a] -= 1
            Trusted[b] += 1

        for i in range(1, len(Trusted)):
            if Trusted[i] == N - 1:
                return i

        return -1

if __name__ == "__main__":
    #N = 2
    #trust = [[1, 2]]
    N = 4
    trust = [[1, 4], [2, 4],[3,4]]

    s = Solution()
    print(s.findJudge(N,trust))
