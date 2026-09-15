class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # validate by char length
        if len(s) != len(t):
            return False
        count = {}
        # map count of char in s 
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # compare mapped char of s with t
        for char in t:
            # char not found in count
            if char not in count:
                return False
            # sub 1 from char count
            count[char] -= 1
            if count[char] < 0:
                return False
        return True