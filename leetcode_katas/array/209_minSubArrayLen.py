class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        s = 0
        minimum = float('inf')

        for right in range(len(nums)):
            s += nums[right]

            while s >= target:
                minimum = min(minimum, right - left + 1)
                s -= nums[left]
                left += 1

        return minimum if minimum != float('inf') else 0
    
            


    
Solution().minSubArrayLen(7, [2,3,1,2,4,3])