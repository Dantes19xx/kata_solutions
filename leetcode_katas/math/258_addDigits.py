class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        dig = int(num)
        arr = []

        while len(str(dig)) > 1:
            while dig > 0:
                arr.append(dig % 10)
                dig //= 10

            dig = sum(arr)
            arr = []

        return dig

Solution().addDigits(0)