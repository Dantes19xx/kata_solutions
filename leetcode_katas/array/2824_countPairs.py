class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        res = 0
        i = 0
        j = len(nums) - 1
        nums.sort()

        while i < j:
            if nums[i] + nums[j] < target:
                res += (j - 1)
                i += 1
            else:
                j -= 1
            
        return res

    
Solution().countPairs([-6,2,5,-2,-7,-1,3], -2)
