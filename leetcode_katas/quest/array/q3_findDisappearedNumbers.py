class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        s = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in s:
                ans.append(i)

        return ans
    
Solution().findDisappearedNumbers([7,3,3,1,2,8,8,4])