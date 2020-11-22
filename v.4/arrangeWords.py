class Solution:
    def arrangeWords(self, text: str) -> str:
        arr = text.split()
        arr[0] = arr[0].lower()
        arr.sort(key=len)
        arr[0] = arr[0].capitalize()

        return " ".join(arr)

