class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        
        return [x for x in hours if x >= target]
    
Solution().numberOfEmployeesWhoMetTarget([0,1,2,3,4], 1)