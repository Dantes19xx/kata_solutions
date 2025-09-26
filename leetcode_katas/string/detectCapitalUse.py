import re


class Solution(object):
    def detectCapitalUse(self, word: str):
        """
        :type word: str
        :rtype: bool
        """
        
        if word.istitle() or word.isupper() or word.islower():
            return True
        
        return False
