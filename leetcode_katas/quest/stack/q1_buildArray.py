class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        
        output = []
        output_digit = []

        for i in range(1, n + 1):
            if output_digit == target:
                return output
            
            output.append("Push")
            output_digit.append(i)

            if i not in target:
                output.append("Pop")
                output_digit.pop()

        return output
    
Solution().buildArray([1, 3], 3)