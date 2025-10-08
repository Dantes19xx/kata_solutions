class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            is_sorted = True
            for j in range(1, len(nums) - i):
                if nums[j - 1] > nums[j]:
                    is_sorted = False
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]

            if is_sorted:
                return nums

        return nums
            


Solution().sortColors([2,0,2,1,1,0])