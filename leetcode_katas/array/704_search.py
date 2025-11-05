class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2

            if target > nums[mid]:
                l = mid + 1

            elif target < nums[mid]:
                r = mid - 1

            else:
                return mid
            
        return -1


    
Solution().search([-1,0,3,5,9,12], 9)