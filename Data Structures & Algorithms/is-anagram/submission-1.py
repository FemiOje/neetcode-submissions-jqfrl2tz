class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter not in char_count:
                char_count[letter] = 1
            else:
                char_count[letter] += 1
        
        for letter in t:
            if letter not in char_count:
                return False
            elif char_count[letter] == 0:
                return False
            else:
                char_count[letter] -= 1
                
        return True;