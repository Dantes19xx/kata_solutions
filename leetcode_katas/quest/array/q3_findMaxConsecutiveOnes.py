class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maximum = float('-inf')
        curr = 0

        for n in nums:
            if n == 1:
                curr += 1
            else:
                if curr > maximum:
                    maximum = int(curr)
                
                curr = 0

        if curr > maximum:
            maximum = int(curr)

        return maximum
    
Solution().findMaxConsecutiveOnes([1,1, 1, 1, 1,0,1,1,0,1, 1, 1, 1])