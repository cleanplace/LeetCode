class Solution:
    def minDistance(self, word1, word2):

        n = len(word1)
        m = len(word2)

        #m,n중 하나가 값이 없을 때
        if n * m == 0:
            return n + m

        #변환 내역을 저장하는 배열 선언
        d = [[0] * (m + 1) for _ in range(n + 1)]

        #row : word1 ,col : word2
        #boundaries 초기화
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j

        #편집거리 계산
        #계산공식 : d[i][j] = 1+min(d[i - 1][j],d[i][j - 1],d[i - 1][j - 1]-1)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + 1
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)

        return d[n][m]

if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"

    s = Solution()
    print(s.minDistance(word1,word2))