from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if k <= 0:
            return nums

        if n - 1 < k:
            return [-1] * n
        
        res = [-1] * k
        prefix = [nums[0]]

        for i in range(1, n):
            prefix.append(prefix[-1] + nums[i])

        for i in range(k, n - k):
            if i == k:
                res.append(prefix[i+k] // (2 * k + 1))
            else:
                res.append((prefix[i+k] - prefix[i-k-1]) // (2 * k + 1))

        res.extend([-1] * (len(nums) - len(res)))    
        
        return res

    
Solution().getAverages([7,4,3,9,1,8,5,2,6], 3)