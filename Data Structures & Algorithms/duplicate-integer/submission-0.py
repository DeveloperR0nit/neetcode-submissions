class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = 1
        for i in range (0,len(nums)-1):
            for j in range(k,len(nums)):
                if nums[i] == nums[j]:
                    return True
            k = k+1        
        return False