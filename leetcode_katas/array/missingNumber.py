class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        l = len(nums)
        if nums[0] != 0:
            return 0

        for i in range(1, l):
            if nums[i] - nums[i - 1] > 1:
                return nums[i - 1] + 1
            
        return nums[-1] + 1


Solution().missingNumber([3, 0, 1])