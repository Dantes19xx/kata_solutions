class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        buffer = set()
        res = []

        for i in nums:
            if i in buffer:
                res.append(i)
            else:
                buffer.add(i)

        return res
    
Solution().getSneakyNumbers([0,3,2,1,3,2])