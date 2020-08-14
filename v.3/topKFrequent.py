"""
692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.

**Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]

Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

**Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]

Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
with the number of occurrence being 4, 3, 2 and 1 respectively.

"""


#sorting
# O(NlogN) / O(N)

import collections

class Solution(object):
    def topKFrequent(self, words, k):
        answer =[]
        count = collections.Counter(words)
        candidates = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        candidates_k =candidates[:k]
        for word, count in candidates_k:
            answer.append(word)
        return answer

# Heap
# O(Nlogk) / O(N)

import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


#trie
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        self.freq = 0

class Solution:
    def topKFrequent(self, words, k):

        def insert(root, word):
            current = root
            for letter in word:
                current = current.children[letter]

            current.is_word = True
            current.freq += 1
            return current.freq

        root = TrieNode()
        a_dict = {}
        res_dict={}
        answer=[]

        for word in words:
            freq = insert(root, word)
            a_dict[word] = freq
        #keys = a_dict.keys()
        res_dict =sorted(a_dict.items(),key = lambda x:x[1],reverse=True)
        for word, count in res_dict:
            answer.append(word)
        return answer[:k]


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2

    s = Solution()
    result =s.topKFrequent(words,k)

    print(result)