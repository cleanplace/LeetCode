#Backtracking 방식
class Solution:
    def generateParenthesis(self, n):
        result = []
        self.dfs(n,result,'',0,0)
        return result

    def dfs(self,n,result,path,left,right):
        a=1
        # 현재 괄호가 유효한지 체크
        if not self.isValid(left,right,n):
            return

        # 2개씩 쌍이 이루어지는지 체크
        if len(path) == n*2:
            result.append(path)
            return
        self.dfs(n,result,path+'(',left+1,right)
        self.dfs(n,result,path+')',left,right+1)

    def isValid(self,left,right,n):
        # 더 검사할 여지가 남아있는 케이스들
        # 열려진 괄호가 더 많거나, n보다 현재 괄호가 적거나
        return left >= right and left <= n and right <= n


#카탈랑수의 순열 공식 활용
class Solution(object):
    def generateParenthesis(self, n):
        if n == 0: return ['']
        ans = []

        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans


if __name__ == "__main__":
    n = 3
    s = Solution()
    print(s.generateParenthesis(n))

