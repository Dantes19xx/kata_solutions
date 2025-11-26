class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.nums = nums
        self.prefix = self.get_prefix_sum()

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        if left == 0:
            return self.prefix[right]
        
        return self.prefix[right] - self.prefix[left-1]

    def get_prefix_sum(self):
        
        prefix = [self.nums[0]]

        for i in range(1, len(self.nums)):
            prefix.append(self.nums[i] + prefix[-1])

        return prefix
        


obj = NumArray([-2, 0, 3, -5, 2, -1])

param_1 = obj.sumRange(0, 2)
param_2 = obj.sumRange(2, 5)
param_3 = obj.sumRange(0, 5)
a = 1
