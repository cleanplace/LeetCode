#O(N)/O(1)
class Solution(object):
    def partitionLabels(self, S):

        ans, last_idx, max_idx, s_length = [] ,{} ,0 , 0
        for i , char in enumerate(S):
            last_idx[char] = i

        for i, char in enumerate(S):
            max_idx = max(max_idx, last_idx[char])
            s_length += 1
            if i == max_idx:
                ans.append(s_length)
                s_length = 0

        return ans

if __name__ == "__main__":
    m = "ababcbacadefegdehijhklij"
    s = Solution()

    print(s.partitionLabels(m))