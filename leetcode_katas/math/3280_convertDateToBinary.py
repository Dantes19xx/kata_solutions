class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        
        date_arr = date.split("-")
        res = []

        for d in date_arr:
            date_dec = int(d)
            date_bin = []
            
            while date_dec > 0:
                date_bin.append(str(date_dec % 2))
                date_dec //= 2
            
            date_bin.reverse()
            res.append("".join(date_bin))
            
        return "-".join(res)
                
    
Solution().convertDateToBinary("2080-02-29")