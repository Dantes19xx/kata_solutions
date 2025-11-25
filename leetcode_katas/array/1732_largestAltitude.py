class Solution:
    def largestAltitude(self, gain) -> int:
        prefix = 0
        maximum = gain[0] if gain[0] > 0 else 0

        for i in range(len(gain)):
            prefix += gain[i]
            if prefix > maximum:
                maximum = int(prefix)

        return maximum

Solution().largestAltitude([-4,-3,-2,-1,4,3,2])