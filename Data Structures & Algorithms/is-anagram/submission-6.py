class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        count = {}

        for character in s:
            if character not in count:
                count[character] = 1
            else:
                count[character] = count[character] + 1
            
        for character in t:
            if character not in count or count[character] == 0:
                return False
            else:
                count[character] = count[character] - 1
        
        return True