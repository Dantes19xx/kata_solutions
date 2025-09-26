class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        res = []
        base = 7
        is_negative = True if num < 0 else False

        if num == 0:
            return "0"

        num = int(abs(num))

        while num > 0:
            res.append(str(num % base))
            num //= base

        res.reverse()

        if is_negative:
            res.insert(0, "-")
            
        return "".join(res)
    
Solution().convertToBase7(-7)