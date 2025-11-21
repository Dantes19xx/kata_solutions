class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]

            if s == target:
                return [left+1, right+1]
            elif s > target:
                right -= 1
            else:
                left += 1

    
Solution().twoSum([2,3,4], 6)