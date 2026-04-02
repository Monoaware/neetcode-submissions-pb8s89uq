class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_groups = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                count[index] = count[index] + 1

            anagram_groups[tuple(count)].append(s)
        
        return list(anagram_groups.values())