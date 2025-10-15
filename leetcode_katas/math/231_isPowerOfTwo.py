class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        is_power_of_two = False
        i = 0

        while not is_power_of_two :
            curr = pow(2, i)

            if curr == n:
                is_power_of_two = True
                return True
            
            if curr > n:
                return False
            
            i += 1



Solution().isPowerOfTwo(16)