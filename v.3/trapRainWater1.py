"""
42. Trapping Rain Water

"""

# stack
class Solution(object):
    def trap(self, height):
        size = len(height)
        stack = []
        result = 0

        for current in range(size):
            while stack and height[stack[-1]] < height[current]:
                top = stack.pop()
                if not stack:
                    break

                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                result += distance * bounded_height

            stack.append(current)

        return result

"""
# Two pointer

class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        ans = left_max = right_max = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans
"""

if __name__ == "__main__":
    a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    result = s.trap(a)

    print(result)