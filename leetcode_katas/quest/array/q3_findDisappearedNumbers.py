class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        nums.sort()
        res = []

        for i in range(1, n):
            if nums[i] - nums[i - 1] > 1:
                res.append(nums[i-1])

        a = 1
    
Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])