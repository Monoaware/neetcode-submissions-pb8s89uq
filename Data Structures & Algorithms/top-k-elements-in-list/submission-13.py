class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Create a dictionary to count frequencies for each number. 
        dictionary = defaultdict(int)

        # Create a bucket to hold each possible frequency. 
        # The worst case scenario here is that we have as many buckets as numbers.
        frequency_bucket = [[] for i in range(len(nums) + 1)]

        # Initialize the dictionary with the frequencies of each number.
        # key -> number; value -> frequency
        for num in nums:
            dictionary[num] = dictionary[num] + 1
    
        # Populate the frequency bucket using the information stored in the dictionary.
        for num, frequency in dictionary.items():
            frequency_bucket[frequency].append(num)

        # Create and populate the result list with the top k most-frequent elements.
        result = []

        for i in range(len(frequency_bucket) - 1, 0, -1):
            for num in frequency_bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result