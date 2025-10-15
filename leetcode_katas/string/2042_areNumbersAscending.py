class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        digit_arr = [x for x in s.split(" ") if x.isdigit()]
        if not digit_arr:
            return False
        
        i = 0

        while i < len(digit_arr) - 1:
            if not int(digit_arr[i]) < int(digit_arr[i + 1]):
                return False
            i += 1

        return True

    
Solution().areNumbersAscending("a puppy has 2 eyes 4 legs")
