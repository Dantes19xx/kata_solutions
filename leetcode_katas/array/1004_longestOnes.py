class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        left = max_s = zeroes_qty = 0

        for right in range(n):
            if nums[right] == 0:
                zeroes_qty += 1               

            if zeroes_qty > k:
                if (right - 1 - left) + 1 > max_s:
                    max_s = (right - 1 - left) + 1

                while zeroes_qty > k:
                    if nums[left] == 0:
                        zeroes_qty -= 1
                
                    left += 1
                
            
        if zeroes_qty <= k:
            if (right - left) + 1 > max_s:
                    max_s = (right - left) + 1

        return max_s


    
Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)