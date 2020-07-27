"""
394. Decode String

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string = ''
        cur_num = 0

        for c in s :
            if c == '[':
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = ''
                cur_num = 0
            elif c == ']':
                num = stack.pop()
                pre_string = stack.pop()
                cur_string = pre_string + num * cur_string

            elif c.isdigit():
                cur_num = cur_num * 10 + int(c) # 10의 자리 이상 처리
            else:
                cur_string += c

        return cur_string


if __name__ == "__main__":

    # s = "3[a]2[bc]"
    s = "3[a2[c]]"
    # s = "2[abc]3[cd]ef"
    # s = "2[abc]3[cd]ef"
    # s = "1000[leetcode]"

    a = Solution()
    result = a.decodeString(s)
    print(result)
