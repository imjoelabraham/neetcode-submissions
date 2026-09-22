class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # without using sort
        if len(s) != len(t):
            return False
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            if char_count.get(char, 0) == 0:
                return False
            char_count[char] -= 1
        return True
