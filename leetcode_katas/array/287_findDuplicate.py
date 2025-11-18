class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        j = len(nums) - 2

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
            
            if nums[j] == nums[j + 1]:
                return nums[j]

            j -= 1
        
        a = 1
    
Solution().findDuplicate([3,1,3,4,2])