class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        
        for i in range(1, len(nums)+1):
            if original in nums:
                original *=2
            else:
                return original
        
        return original

    
Solution().findFinalValue([2], 2)