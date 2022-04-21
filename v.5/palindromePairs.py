## Approach 1: Brute force
def palindromePairs(self, words: List[str]) -> List[List[int]]:

    pairs = []

    for i, word_1 in enumerate(words):
        for j, word_2 in enumerate(words):
            if i == j:
                continue
            combined_word = word_1 + word_2
            if combined_word == combined_word[::-1]:
                pairs.append([i, j])

    return pairs



## Approach 2: Hashing
class Solution:
    def palindromePairs(self, words):

        def is_palindrome(check):
            return check == check[::-1] #문자열을 거꾸로 출력

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, idx in words.items():
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back], idx])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([idx, words[back]])
        return valid_pals

if __name__ == "__main__":

    words = ["abcd", "dcba", "lls", "s", "sssll"]

    s = Solution()
    print(s.palindromePairs(words))

