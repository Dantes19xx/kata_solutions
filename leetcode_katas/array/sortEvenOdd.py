class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if len(nums) <= 2:
            return nums

        odd_arr = [nums[x]for x in range(len(nums)) if x % 2 != 0]       
        even_arr = [nums[x]for x in range(len(nums)) if x % 2 == 0]

        odd_arr.sort(reverse=True)
        even_arr.sort()

        res = []

        for i in range(len(odd_arr)):
            res.extend([even_arr[i], odd_arr[i]])

        if len(even_arr) > len(odd_arr):
            res.append(even_arr[-1])

        return res

    
Solution().sortEvenOdd([5,39,33,5,12,27,20,45,14,25,32,33,30,30,9,14,44,15,21])