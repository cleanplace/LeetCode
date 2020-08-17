# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = collections.defaultdict(list)
#         for s in strs:
#             ans[tuple(sorted(s))].append(s)
#         return ans.values()

class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in dic:
                dic.get(key).append( str )
            else:
                dic[key] = [str]
        return dic.values()

if __name__ == "__main__":
    str_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s=Solution()
    result=s.groupAnagrams(str_list)

    print(result)