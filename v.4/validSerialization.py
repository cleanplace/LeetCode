class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1

        for node in preorder.split(','):
            slots -= 1

            if slots < 0:
                return False

            if node != '#':
                slots += 2

        return slots == 0


if __name__ == "__main__":
    input = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    #input="9,#,#,1"

    s = Solution()
    print(s.isValidSerialization(input))