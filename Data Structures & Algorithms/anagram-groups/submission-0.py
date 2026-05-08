class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs1 = strs
        strs2 = []
        while len(strs1) > 0 :
            l = []
            j = 1
            while j<len(strs1):
                li = list(strs1[0])
                lj = list(strs1[j])
                li.sort()
                lj.sort()
                if li == lj:
                    l.append(strs1[j])
                    del strs1[j]
                else:
                    j = j+1
            l.append(strs1[0])
            strs2.append(l)
            del strs1[0]
        return strs2


        