import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):

        if not nums1 or not nums2 or not k: return []
        i = j = 0
        minHeap = []

        for _ in range(k):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    for x in nums2[j:]: heapq.heappush(minHeap, (nums1[i], x))
                    i += 1
                else:
                    for x in nums1[i:]: heapq.heappush(minHeap, (x, nums2[j]))
                    j += 1

        return heapq.nsmallest(k, minHeap, key=sum)