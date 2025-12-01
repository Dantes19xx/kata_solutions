class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        space = i = 0
        res = []

        while space != k and i < len(s):
            if s[i] == " ":
                space += 1
            
            res.append(s[i])

            i += 1

        return "".join(res).rstrip()
        
    
Solution().truncateSentence("What is the solution to this problem", 11)
