class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        if not chars:
            return []
        
        qount = 0
        prev = None
        insertion_id = 0

        for i in range(len(chars)):
            if prev is None:
                qount += 1
                prev = chars[i]

            elif prev != chars[i]:
                chars[insertion_id] = prev
                prev = chars[i]
                insertion_id += 1
                if qount > 1:
                    for j in str(qount):
                        chars[insertion_id] = j
                        insertion_id += 1
                qount = 1
                
            else:
                qount += 1

        chars[insertion_id] = prev
        prev = chars[i]
        insertion_id += 1
        if qount > 1:
            for j in str(qount):
                chars[insertion_id] = j
                insertion_id += 1

        return insertion_id
    
Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])