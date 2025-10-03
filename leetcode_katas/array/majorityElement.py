from math import ceil

class Solution(object):
    def majorityElement(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maj_el_qty = len(nums) // 2
        maj_el_val = float('inf')
        curr_qty = 0
        s = list(set(nums))
        i = 0

        while curr_qty <= maj_el_qty and i < len(s):
            curr_val = s[i]
            curr_qty = nums.count(curr_val)
            if curr_qty >= maj_el_qty:
                return curr_val
            
            i += 1


Solution().majorityElement([3,2,3])