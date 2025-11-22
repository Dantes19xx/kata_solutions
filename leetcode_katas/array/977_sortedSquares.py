class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l = 0
        r = len(nums) - 1

        while l <= r:
            if l != r:
                nums[l] *= nums[l]
                nums[r] *= nums[r]
            
            else:
                nums[l] *= nums[l]
            
            l += 1
            r -= 1

        nums.sort()

        return nums
        
    
Solution().sortedSquares([-4,-1,0,3,10])