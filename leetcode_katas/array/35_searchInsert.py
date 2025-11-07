class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return 1 if target > nums[0] else 0

        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                l = mid + 1
            
            else: 
                r = mid - 1
        
        return l

    
Solution().searchInsert([1,3,5,6], 0)