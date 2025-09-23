from collections import deque

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.bitwise_res = self.transform_to_bit(n)      

        if len(self.bitwise_res) < 32:
            self.add_lead_zeroes()

        self.reverted_bit_array = self.revert_bit()
        self.transform_to_10()

        return self.res_in_10   
        
    
    def transform_to_bit(self, digit):
        binary_array = deque()

        if digit == 0:
            binary_array.appendleft(0)

        while digit > 0:
            single_dig = digit % 2
            binary_array.appendleft(single_dig)
            digit = digit // 2

        return binary_array
    
   
    def add_lead_zeroes(self):
        while len(self.bitwise_res) < 32:
            self.bitwise_res.appendleft(0)

    def revert_bit(self):
        return list(reversed(self.bitwise_res))
    

    def transform_to_10(self):
        res_in_10 = 0
        for bit in self.reverted_bit_array:
            res_in_10 = res_in_10 * 2 + bit
        self.res_in_10 = res_in_10


res = Solution().reverseBits(43261596)

a = 1
b = 2