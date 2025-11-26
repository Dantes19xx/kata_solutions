class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        letters = [ch for ch in s if ch.isalpha()]
        letters.reverse()    
        
        result = []
        idx = 0 

        for ch in s:
            if ch.isalpha():
                result.append(letters[idx])
                idx += 1
            else:
                result.append(ch) 
        return "".join(result)

Solution().reverseOnlyLetters("a-bC-dEf-ghIj")