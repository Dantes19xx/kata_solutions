class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = [x for x in nums if x != 0]

        max_neg = 0
        max_pos = 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2

            if nums[mid] < 0:
                max_neg += (mid - l) + 1
                l = mid + 1
            
            else:
                max_pos += (r - mid) + 1
                r = mid - 1
            
        return max_neg if max_neg > max_pos else max_pos


    
Solution().maximumCount([5,20,66,1314])