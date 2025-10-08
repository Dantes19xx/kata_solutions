class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 1:
            return 0
        
        nums.sort()
        max_gap = 0

        for i in range(1, len(nums)):
            if abs(nums[i - 1] - nums[i]) > max_gap:
                max_gap = abs(nums[i - 1] - nums[i])

        return max_gap

    
Solution().maximumGap([3,6,9,1])