class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = set(nums)

        for i in range(0, len(n)+1):
            if i not in n:
                return i
    
Solution().missingNumber([9,6,4,2,3,5,7,0,1])