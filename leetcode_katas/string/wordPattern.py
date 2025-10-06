class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            if char_to_word.get(c, w) != w or word_to_char.get(w, c) != c:
                return False
            char_to_word[c] = w
            word_to_char[w] = c

        return True
        

    
Solution().wordPattern("abba", "dog cat cat cat")
