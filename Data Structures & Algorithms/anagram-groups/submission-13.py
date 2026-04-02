class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        letter_array = [0] * 26
        anagram_dict = defaultdict(list)

        for string in strs:

            for character in string:
                numerical_representation = ord(character) - ord('a')
                letter_array[numerical_representation] = letter_array[numerical_representation] + 1

            key = tuple(letter_array)
            anagram_dict[key].append(string)

            letter_array = [0] * 26

        return list(anagram_dict.values())
        