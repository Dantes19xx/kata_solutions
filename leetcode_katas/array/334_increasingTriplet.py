class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n 
            elif n <= second:
                second = n 
            else:
                return True 

        return False
        
    
Solution().increasingTriplet([10, 9, 2, 8, 3, 7, 4])
