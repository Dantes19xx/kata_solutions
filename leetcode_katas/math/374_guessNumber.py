# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

def guess(i):
    pass

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        a = 1702766719
        l = 1
        r = int(n)
        pick = l + ((r - l) // 2)
        guess_res = None

        while guess_res != 0:
            if pick < a:
                guess_res = 1
            elif pick > a:
                guess_res = -1
            else:
                guess_res = 0

            if guess_res == 1:
                l = pick + 1
            elif guess_res == -1:
                r = pick - 1

            else:
                return pick
            
            pick = l + ((r - l) // 2)
            
        return None
            

    

Solution().guessNumber(2126753390)