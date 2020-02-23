def decodeString(self, s: str) -> str:

    stack = []
    result = ""
    i, n = 0, len(s)

    while i < n:
        if s[i].isdigit():
            num = ""
            while i < n and s[i].isdigit():
                num += s[i]
                i += 1

            i += 1
            string = ""

            while i < n and s[i].isalpha():
                string += s[i]
                i += 1
            stack.append([int(num), string])
            continue

        if s[i] == ']':
            num, string = stack.pop()
            string = string * num
            i += 1
        else:
            string = ""
            while i < n and s[i].isalpha():
                string += s[i]
                i += 1

        if stack:
            stack[-1][1] += string
        else:
            result += string

    return result