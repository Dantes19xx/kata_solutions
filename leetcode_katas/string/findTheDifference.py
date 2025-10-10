class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        s = [ord(x) for x in s]
        s = self.bubble_sort(s)
        t = [ord(x) for x in t]
        t = self.bubble_sort(t)
        
        for i in range(len(t) - 1):
            if s[i] != t[i]:
                return chr(t[i])
            
        return chr(t[-1])

    def bubble_sort(self, arr):

        for i in range(len(arr)):
            for j in range(1, len(arr) - i):
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]

        return arr



Solution().findTheDifference("abcdz", "abxcdz")