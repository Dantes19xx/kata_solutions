class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        
        lesser = [x for x in nums if x < pivot]
        greater = [x for x in nums if x > pivot]
        pivot_ = [x for x in nums if x == pivot]

        return lesser + pivot_ +  greater

    
print(Solution().pivotArray([-3,4,3,2], 2))