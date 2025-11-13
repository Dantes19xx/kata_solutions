class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums.sort()
        duplicate = 0
        missed = 0

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                duplicate = int(nums[i])
            
            elif nums[i] - nums[i - 1] > 1:
                missed = nums[i] - 1

            
        if missed == 0:
            if nums[0] != 1:
                missed = 1
            else:
                missed = nums[-1] + 1
            
        return [duplicate, missed]
                
    
# Solution().findErrorNums([1,5,3,2,2,7,6,4,8,9])
Solution().findErrorNums([2,2])