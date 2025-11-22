class Solution:
    def waysToSplitArray(self, nums):
        if len(nums) < 2:
            return 0
        
        total = sum(nums)
        left = 0
        res = 0

        for i in range(len(nums) - 1):
            left += nums[i]
            right = total - left
            if left >= right:
                res += 1

        return res


Solution().waysToSplitArray([-5, -3, -2, -1])
    
