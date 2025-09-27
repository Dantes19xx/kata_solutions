class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num == 0:
            return "0"
        elif num < 0:
            # num = num % pow(2, 32) #num & 0xFFFFFFFF
            num = pow(2, 32) - abs(num)

        # 4294967295 num = num % pow(2, 32)

        hexal_digits = [10, 11, 12, 13, 14, 15]
        base = 16
        res = []


        while num > 0:
            curr = num % base
            res.append(str(curr) if curr not in hexal_digits else chr(curr + 87))
            num //= base

        res.reverse()

        return "".join(res)



Solution().toHex(-1)