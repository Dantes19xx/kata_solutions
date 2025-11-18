class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        
        left = 0

        while len(bits[left:]) >= 2:
            if bits[left] == 1:
                left += 2

            else:
                left += 1

        if not bits[left:]:
            return False
        
        return True
            

    
Solution().isOneBitCharacter([0,1,0])