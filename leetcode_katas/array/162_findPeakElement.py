class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0 
        r = len(nums) - 1

        while l < r:
            mid = (r + l) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l
    
Solution().findPeakElement([1, 2])