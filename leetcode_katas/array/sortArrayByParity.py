class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        even_arr = [x for x in nums if x % 2 == 0]
        odd_arr = [x for x in nums if x % 2 != 0]

        return even_arr + odd_arr



Solution().sortArrayByParity([3,1,2,4])