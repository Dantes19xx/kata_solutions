class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        self.sentence = s.split()
        return len(self.sentence[-1])
        
    
Solution().lengthOfLastWord("Today is a nice day")