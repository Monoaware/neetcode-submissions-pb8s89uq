class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maximum_length = 0
        hashset = set()
        left = 0

        for right in range(len(s)):
            if s[right] not in hashset:
                hashset.add(s[right])

                current_length = right - left + 1

                if current_length > maximum_length:
                    maximum_length = current_length
                
            else:
                while s[right] in hashset:
                    hashset.remove(s[left])
                    left = left + 1

                hashset.add(s[right])
                
        return maximum_length