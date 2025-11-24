class Solution:
    def minStartValue(self, nums):
        minimum = float("inf")
        prefix = 0

        for i in nums:
            prefix += i
            if prefix < minimum:
                minimum = int(prefix)
            
            
        if minimum >= 1:
            return 1

        return 1 - minimum
            
    
Solution().minStartValue([-12])
        