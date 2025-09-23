from collections import deque


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        self.digit = x
        d = deque()

        while self.digit > 0:
            d.append(self.digit % 10)
            self.digit = self.digit // 10

        while len(d) != 0:
            if len(d) > 1:
                if (d.popleft() != d.pop()):
                    return False
            else:
                return True
            
        return True

Solution().isPalindrome(1291)