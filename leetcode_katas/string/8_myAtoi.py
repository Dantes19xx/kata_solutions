class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        top_border = 2147483647
        bot_border = -2147483648

        s = s.lstrip()
        neg_sign = 1
        if s.startswith("-"):
            neg_sign = -1
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]

        i = 0
        res = ""

        while i < len(s) and s[i].isdigit():
            res += s[i]
            i += 1


        if res:
            res = int(res) * neg_sign
            if res < bot_border:
                return bot_border
            
            if res > top_border:
                return top_border
            
            return res
        
        return 0


Solution().myAtoi("   -042")
