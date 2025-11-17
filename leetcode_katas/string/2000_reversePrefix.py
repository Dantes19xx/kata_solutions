class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
        try:
            pivot = word.index(ch)
        except:
            return word
        
        return word[pivot::-1] + word[pivot+1:]
    
Solution().reversePrefix("xyxzxe", "z")