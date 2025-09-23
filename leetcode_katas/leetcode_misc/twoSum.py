class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
            
        a = 1
    

Solution().twoSum([3,2,3], 6)