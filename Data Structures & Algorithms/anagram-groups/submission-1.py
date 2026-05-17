class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)
        for a in strs:
            l = [0]*26
            for b in a:
                l[ord(b) - ord("a")] += 1
            dic[tuple(l)].append(a)
        return (list(dic.values()))