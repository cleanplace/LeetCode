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
