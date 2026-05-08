class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        tList = list(t)
        print(sList)
        print(tList)     
        if len(sList) == len(tList):
            while len(sList) > 0 and len(tList) > 0:
                c = sList[0]
                if c in tList:
                    sList.remove(c)
                    tList.remove(c)
                else:
                    break
            if len(sList) == 0 and len(tList) == 0:
                return True
            else :
                return False
        else :
            return False