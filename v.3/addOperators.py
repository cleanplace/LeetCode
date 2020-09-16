class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):

            # Done processing all the digits in num
            if index == N:

                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:

                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            string.append('+'); string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:

                # SUBTRACTION
                string.append('-'); string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(0, 0, 0, 0, [])
        return answers


###
# def addOperators(self, num, target):
#     res, self.target = [], target
#     for i in range(1,len(num)+1):
#         if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
#             self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
#     return res
#
# def dfs(self, num, temp, cur, last, res):
#     if not num:
#         if cur == self.target:
#             res.append(temp)
#         return
#     for i in range(1, len(num)+1):
#         val = num[:i]
#         if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
#             self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
#             self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
#             self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)
#
if __name__ == "__main__":

    num = "123"
    target = 6

    s = Solution()
    print(s.addOperators(num,target))