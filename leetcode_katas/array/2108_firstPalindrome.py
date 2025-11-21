class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        i = 0
        j = len(words) - 1
        pal_in_left_ind = float('inf')
        pal_in_right_ind = float('inf')

        while i <= j:
            if words[i] == words[i][::-1] and i < pal_in_left_ind:
                pal_in_left_ind = int(i)
            i += 1

            if words[j] == words[j][::-1] and j < pal_in_right_ind:
                pal_in_right_ind = int(j)
            j -= 1
      
        min_idx = min(pal_in_right_ind, pal_in_left_ind)
       
        return words[min_idx] if min_idx != float('inf') else ""
                
    
Solution().firstPalindrome(["abc","bdab","car","adca","racdecar","cool"]) #ada