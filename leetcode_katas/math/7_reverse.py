class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        top_border = 2147483647
        bot_border = -2147483648

        res = "" if x >=0 else "-"
        x = abs(x)

        while x > 0:
            curr = x % 10
            res += str(curr)
            if int(res) <= bot_border or int(res) >= top_border:
                return 0
            
            x //= 10

        if not res or res == "-":
            return 0
        
        return int(res)



    
Solution().reverse(0)