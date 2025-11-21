class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        word_arr = s.split(" ")
        rev = [w[::-1] for w in word_arr]
        return " ".join(rev)

    
Solution().reverseWords("Let's take LeetCode contest")