class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        return max([sum(i) for i in accounts])


Solution().maximumWealth([[1,5],[7,3],[3,5]])