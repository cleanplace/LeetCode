class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != 0:
                    top = matrix[row - 1][col] if row > 0 else float('inf')
                    left = matrix[row][col - 1] if col > 0 else float('inf')

                    matrix[row][col] = min(top, left) + 1

        for row in range(rows)[::-1]:
            for col in range(cols)[::-1]:
                if matrix[row][col] != 0:
                    bottom = matrix[row + 1][col] if row < rows - 1 else float('inf')
                    right = matrix[row][col + 1] if col < cols - 1 else float('inf')

                    matrix[row][col] = min(matrix[row][col], min(bottom, right) + 1)

        return matrix


