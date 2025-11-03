class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        maximum = max(candies)
        return [i + extraCandies >= maximum for i in candies]


Solution().kidsWithCandies([12,1,12], 10)