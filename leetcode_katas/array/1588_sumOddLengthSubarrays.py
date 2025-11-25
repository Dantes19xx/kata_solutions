class Solution:
    def sumOddLengthSubarrays(self, arr):
        prefix = [arr[0]]

        if len(arr) == 1:
            return arr[0]
        
        for i in range(1, len(arr)):
            prefix.append(arr[i] + prefix[-1])

        if len(arr) < 2:
            i = 0
        else:
            i = 2
        res = 0
        
        while i < len(prefix):
            shift = 0
            for j in range(i, len(prefix)):
                if shift == 0:
                    res += prefix[j]
                else:
                    res += prefix[j] - prefix[j - i - 1]

                shift += 1

            i += 2

        res += prefix[-1]
        return res
    
Solution().sumOddLengthSubarrays([1])
        