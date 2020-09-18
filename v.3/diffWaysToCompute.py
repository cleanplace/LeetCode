#O(N*logN)/O(N) : 최악 O(N^2)/O(N)
class Solution:
    def diffWaysToCompute(self, input):
        return self.helper(input, {})

    def helper(self, input, seen):
        if input in seen:
            return seen[input]
        if input.isnumeric():
            return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in "+-*":
                res += [l + r if c == "+" else l - r if c == "-" else l * r
                        for l in self.helper(input[:i], seen)
                        for r in self.helper(input[i + 1:], seen)]
        seen[input] = res
        return res

if __name__ == "__main__":
    #input = "2-1-1"
    input = "2*3-4*5"

    s = Solution()
    print(s.diffWaysToCompute(input))