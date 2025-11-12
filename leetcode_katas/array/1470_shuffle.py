class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        x = nums[:n]
        y = nums[n:]

        res = []

        for i in range(n):
            res.extend([x[i], y[i]])

        return res


Solution().shuffle([1,2,3,4,4,3,2,1], 4)

