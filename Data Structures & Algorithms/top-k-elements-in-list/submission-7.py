class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictionary = defaultdict(int)

        for num in nums:
            dictionary[num] = dictionary[num] + 1

        array = []

        # Remember that the key is the number and the value is the frequency.
        for key, value in dictionary.items():
            array.append([value, key])
        
        array.sort()

        result = []

        for entry in array[::-1][:k]:
            result.append(entry[1])

        return result
        