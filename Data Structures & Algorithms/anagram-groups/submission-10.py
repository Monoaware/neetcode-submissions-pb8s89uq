class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_strs = list()

        for string in strs:
            string = ''.join(sorted(string))
            sorted_strs.append(string)

        strs_dict = defaultdict(list)

        for i in range(len(sorted_strs)):
            strs_dict[sorted_strs[i]].append(strs[i])
        
        return list(strs_dict.values())
        