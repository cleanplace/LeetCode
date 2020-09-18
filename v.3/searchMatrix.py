class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)

if __name__ == "__main__":
    input=[
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    s=Solution()
    print(s.searchMatrix(input,5))