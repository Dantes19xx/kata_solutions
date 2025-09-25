class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        twice = set()

        for c in s:
            if c in twice:
                return c
            
            twice.add(c)
            