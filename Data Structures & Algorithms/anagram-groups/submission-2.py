class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)
        for a in strs:
            dic[tuple(sorted(a))].append(a)
        return (list(dic.values()))