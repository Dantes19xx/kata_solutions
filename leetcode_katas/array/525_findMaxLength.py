class Solution(object):
    def findMaxLength(self, nums):
        prefix = 0
        first = {0: -1}
        max_len = 0

        for i, x in enumerate(nums):
            prefix += 1 if x == 1 else -1

            if prefix in first:
                max_len = max(max_len, i - first[prefix])
            else:
                first[prefix] = i

        return max_len

print(f"ANSWER==={Solution().findMaxLength([0,1,0,1,1])}")