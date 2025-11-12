class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
        res = 0

        for i in stones:
            if i in jewels:
                res += 1

        return res
    
Solution().numJewelsInStones("aA", "aAAbbbb")