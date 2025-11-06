class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if k <= 1:
            return 0
        
        l = 0
        r = 0
        n = len(nums)
        sub_arr_qty = 0
        product = 1

        for r in range(n):
            product *= nums[r]

            while product >= k: # Уменьшаем окно, пока произведение элементов подмассива не будет меньше k
                product //= nums[l]
                l += 1

            sub_arr_qty += (r - l + 1) # количество подмассивов, которые заканчиваются на r-тый элемент

        return sub_arr_qty



    
Solution().numSubarrayProductLessThanK([10,5,2,6], 100)