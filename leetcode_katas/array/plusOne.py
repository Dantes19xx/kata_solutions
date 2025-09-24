class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
    
        counter = len(digits) - 1
        zeroes = []

        while counter != -1 and digits[counter] == 9:
            if digits[counter] == 9:
                zeroes.append(0)
                digits.pop()

            counter -= 1

        if not digits:
            return [1] + zeroes
        
        digits[-1] = (digits[-1] + 1)

        return digits + zeroes


Solution().plusOne([9, 1, 9])

# [1,2,3]

# [9]