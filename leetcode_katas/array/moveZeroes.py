class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        last_non_zero = 0

        for i in range(l):
            if nums[i] != 0:
                nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
                last_non_zero += 1

        a = 1



Solution().moveZeroes([1,1,0,3,12]) #[1,3,12,0,0]