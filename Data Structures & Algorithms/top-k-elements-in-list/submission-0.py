class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        items = sorted(dic.items(), key=lambda x : x[1], reverse=True)
        l = []
        for i in range(k):
            l.append(items[i][0])
        return l

        