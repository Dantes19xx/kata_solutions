class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = []

        for i in range(len(nums)):
            less = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    less += 1
            
            res.append(less)

        return res
    
Solution().smallerNumbersThanCurrent([7,7,7,7])
