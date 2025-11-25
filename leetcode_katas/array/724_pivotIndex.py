from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        if prefix[-1] - prefix[0] == 0:
            return 0

        for i in range(1, len(nums) - 1):
            if prefix[i - 1] ==  prefix[-1] - prefix[i]:
                return i
            
        if len(nums) - 2 and prefix[-2] == 0:
            return len(nums) - 1
            
        return -1
    
Solution().pivotIndex([1,2, 3])